# Changelog

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