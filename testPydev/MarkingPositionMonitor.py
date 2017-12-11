import json

m1 = """{"type": "NEW",
    "symbol": "APPL",
    "order_id": 1,
    "side": "SELL",
    "quantity": 900,
    "time": "2016-12-22T12:06:04.519266"}"""

m2 = """{
        "type": "ORDER_ACK",
        "order_id": 1,
        "time": "2016-12-22T12:06:04.519488"
        }"""

m3 = """{
        "type": "CANCEL",
        "order_id": 1,
        "time": "2016-12-22T12:05:04.519645"
        }"""

m4 = """{
        "type":"CANCEL_ACK",
        "order_id": 1,
        "time": "2016-12-22T12:06:04.519803"
        }"""

m5 = """{
        "type": "NEW",
        "symbol": "AAPL",
        "order_id": 2,
        "side": "BUY",
        "quantity": 400,
        "time": "2016-12-22T12:06:04.520013"
        }"""

m6 = """{
        "type": "ORDER_REJECT",
        "order_id": 2,
        "reason": "FIRM_RISK_LIMIT_EXCEEEDED",
        "time": "2016-12-22T12:06:04.520190"
        }"""

m7 = """{
        "type": "NEW",
        "symbol": "AAPL",
        "order_id": 3,
        "side": "BUY",
        "quantity": 1800,
        "time": "2016-12-22T12:06:04.520492"
        }"""

m8 = """{
        "type":"ORDER_ACK",
        "order_id": 3,
        "time": "2016-12-22T12:06:04.520660"
        }"""

m9 = """{
        "type": "FILL",
        "order_id": 3,
        "filled_quantity": 1800,
        "remaining_quantity": 0,
        "time": "2016-12-22T12:06:04.520839"
        }"""

m10 = """{
        "type": "NEW",
        "symbol": "AAPL",
        "order_id": 4,
        "side": "SELL",
        "quantity": 1100,
        "time": "2016-12-22T12:06:04.520992"
        }"""

m11 = """{
        "type":"ORDER_REJECT",
        "order_id": 4,
        "time": "2016-12-22T12:06:04.521238"
        }"""

m4 = """{
        "type":"CANCEL",
        "order_id": 3,
        "time": "2016-12-22T12:06:04.521345"
        }"""

m4 = """{
        "type":"CANCEL_REJECT",
        "order_id": 3,
        "reason": "CANNOT_CANCEL_ZERO_QUANTITY",
        "time": "2016-12-22T12:06:04.521456"
        }"""

msg = json.loads(m1)
print msg["order_id"]

class MarkingPositionMonitor():
    def __init__(self):
        pass

    def on_event(self, message):
        json.loads()