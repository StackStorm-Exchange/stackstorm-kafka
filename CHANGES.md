# Changelog

## 2.0.0

* Update to kafka-python 2.0.2 to support python 3.8. #16 by @murthysrd
  This is a major version bump as topics will no longer be auto-created
  by the sensors or by the produce action even if the Kafka server is
  configured to auto-create the topics and partitions.

## 1.0.0

* Drop Python 2.7 support

## 0.2.6

- Convert topic to string in Python 3. Fixes #12

## 0.2.5

- Add explicit support for Python 2 and 3

## 0.2.4

- `ProduceResponse` has no `__dict__` attribute. So this version changes the `produce.py` to return the results of the `_as_dict` method instead

## 0.2.3

- Sensor payload parameter schema for ``KafkaMessageSensor`` and ``KafkaGCPMessageSensor`` sensor
  has been fixed so trigger dispatching works correctly under StackStorm >= 2.9.0 where trigger
  payload validation is enabled by default. #7 #8
