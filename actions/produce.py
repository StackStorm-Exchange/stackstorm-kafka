"""
Kafka Producer Action for stackstorm
"""
import json

from st2common.runners.base_action import Action
from kafka import KafkaProducer, KafkaConsumer


class ProduceMessageAction(Action):
    """
    Action to send messages to Apache Kafka system.
    """

    DEFAULT_CLIENT_ID = "st2-kafka-producer"

    def run(self, topic, message, hosts=None):
        """
        Simple round-robin synchronous producer to send one message to one topic.

        :param hosts: Kafka hostname(s) to connect in host:port format.
                      Comma-separated for several hosts.
        :type hosts: ``str``
        :param topic: Kafka Topic to publish the message on.
        :type topic: ``str``
        :param message: The message to publish.
        :type message: ``str``

        :returns: Response data: `topic`, target `partition` where message was sent,
                  `offset` number and `error` code (hopefully 0).
        :rtype: ``dict``
        """

        if hosts:
            _hosts = hosts
        elif self.config.get("hosts", None):
            _hosts = self.config["hosts"]
        else:
            raise ValueError("Need to define 'hosts' in either action or in config")

        # set default for empty value
        _client_id = self.config.get("client_id") or self.DEFAULT_CLIENT_ID

        consumer = KafkaConsumer(
            bootstrap_servers=_hosts.split(","), client_id=_client_id
        )
        try:
            assert topic in consumer.topics()
        except AssertionError as exc:
            raise AssertionError(f"{topic} does not exist.") from exc

        producer = KafkaProducer(
            bootstrap_servers=_hosts.split(","),
            client_id=_client_id,
            value_serializer=lambda m: m.encode("utf-8"),
            max_request_size=10485760,
        )
        result = producer.send(topic, message)
        record_metadata = result.get(timeout=10)
        return record_metadata
