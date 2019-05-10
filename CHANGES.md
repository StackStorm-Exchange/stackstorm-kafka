# Changelog

## 0.2.3

- Sensor payload parameter schema for ``KafkaMessageSensor`` and ``KafkaGCPMessageSensor`` sensor
  has been fixed so trigger dispatching works correctly under StackStorm >= 2.9.0 where trigger
  payload validation is enabled by default. #7 #8
