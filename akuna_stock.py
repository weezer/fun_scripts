import json

class MarkingPositionMonitor:
    def __init__(self):
        self.orders = {}
        self.markingPosition = {}

    def on_event(self, message):
        msg = json.loads(message)
        event_type = msg['type']
        if event_type == 'NEW':
            return self.new_event(msg)
        elif event_type == 'ORDER_ACK':
            return self.order_ack(msg)
        elif event_type == 'ORDER_REJECT':
            return self.order_reject(msg)
        elif event_type == 'CANCEL':
            return self.cancel(msg)
        elif event_type == 'CANCEL_ACK':
            return self.cancel_ack(msg)
        elif event_type == 'CANCEL_REJECT':
            return self.cancel_reject(msg)
        elif event_type == 'FILL':
            return self.fill(msg)
        else:
            raise ValueError("Message type unknown!")

    def new_event(self, msg):
        side = msg.get('side', None)
        if not side:
            raise ValueError("Invalid side, get: " + side)
        symbol = msg.get('symbol', None)
        if not symbol:
            raise ValueError('Invalid symbol, get:' + symbol)
        quantity = msg.get('quantity', 0)
        time = msg.get('time', 0)

        self.orders[msg['order_id']] = {
            'side': side,
            'remaining': quantity,
            'filled': 0,
            'time': time,
            'symbol': symbol,
            'ack': 0,
        }
        self.markingPosition.setdefault(symbol, 0)
        if side == 'BUY':
            pass
        elif side == 'SELL':
            self.markingPosition[symbol] -= msg.get('quantity', 0)
        return self.markingPosition[symbol]

    def order_ack(self, msg):
        order_id = msg['order_id']
        self.orders[order_id]['ack'] = 1
        symbol = self.orders[order_id]['symbol']
        return self.markingPosition[symbol]

    def order_reject(self, msg):
        order_id = msg['order_id']
        self.orders[order_id]['ack'] = -1
        symbol = self.orders[order_id]['symbol']
        if self.orders[order_id]['side'] == 'SELL':
            self.markingPosition.setdefault(symbol, 0)
            self.markingPosition[symbol] += self.orders[order_id]['remaining']
        return self.markingPosition[symbol]

    def cancel(self, msg):
        order_id = msg['order_id']
        symbol = self.orders[order_id]['symbol']
        return self.markingPosition[symbol]

    def cancel_ack(self, msg):
        order_id = msg['order_id']
        self.orders[order_id]['ack'] = -1
        symbol = self.orders[order_id]['symbol']
        if self.orders[order_id]['side'] == 'SELL':
            self.markingPosition.setdefault(symbol, 0)
            self.markingPosition[symbol] += self.orders[order_id]['remaining']
        return self.markingPosition[symbol]

    def cancel_reject(self, msg):
        order_id = msg['order_id']
        symbol = self.orders[order_id]['symbol']
        return self.markingPosition[symbol]

    def fill(self, msg):
        order_id = msg['order_id']
        symbol = self.orders[order_id]['symbol']
        filled = msg.get('filled_quantity', 0)
        if filled > self.orders[order_id]['remaining']:
            filled = self.orders[order_id]['remaining']
            self.orders[order_id]['remaining'] = 0
            self.orders[order_id]['filled'] += filled
        else:
            self.orders[order_id]['remaining'] -= filled
            self.orders[order_id]['filled'] += filled
        if self.orders[order_id]['side'] == 'BUY':
            self.markingPosition.setdefault(symbol, 0)
            self.markingPosition[symbol] += filled
        return self.markingPosition[symbol]



def assertEqual(a, b):
    if a != b:
        print("False! ", a, b)
    else:
        print(a)

if __name__ == '__main__':
    print("###### test 1 ########")
    M = MarkingPositionMonitor()
    str = json.dumps({"type": "NEW", "symbol": "MIMP", "order_id": 0, "side": "BUY", "quantity": 800,
                      "time": "2017-03-15T10:15:10.975187"})
    # print(M.on_event(str))  #800 1
    assertEqual(M.on_event(str), 0)  # 1

    str = json.dumps({"type": "NEW", "symbol": "IMIMP", "order_id": 1, "side": "SELL", "quantity": 800, "time": "2017-03-15T10:15:10.975187"})
    # print(M.on_event(str))  #800 1
    assertEqual(M.on_event(str), -800) # 1

    str = json.dumps({"type": "ORDER_REJECT", "order_id": 1, "reason": "SYMBOL_UNKNOWN", "time": "2017-03-15T10:15:10.975332"})
    # print(M.on_event(str)) #0 2
    assertEqual(M.on_event(str), 0) # 2

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 2, "side": "BUY", "quantity": 2000, "time": "2017-03-15T10:15:10.975492"})
    # print(M.on_event(str)) #0 3
    assertEqual(M.on_event(str), 0) # 3

    str = json.dumps({"type": "ORDER_ACK", "order_id": 2, "time": "2017-03-15T10:15:10.975606"})
    # print(M.on_event(str)) #0 4
    assertEqual(M.on_event(str), 0)  # 4

    str = json.dumps({"type": "FILL", "order_id": 2, "filled_quantity": 2000, "remaining_quantity": 0, "time": "2017-03-15T10:15:10.975717"})
    #print(M.on_event(str)) #2000 5
    assertEqual(M.on_event(str), 2000)  # 5

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 3, "side": "SELL", "quantity": 700, "time": "2017-03-15T10:15:10.975860"})
    #print(M.on_event(str)) #1300 6
    assertEqual(M.on_event(str), 1300)  # 6

    str = json.dumps({"type": "ORDER_ACK", "order_id": 3, "time": "2017-03-15T10:15:10.975966"})
    #print(M.on_event(str)) #1300  7
    assertEqual(M.on_event(str), 1300)  # 7

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 4, "side": "SELL", "quantity": 1500, "time": "2017-03-15T10:15:10.976067"})
    #print(M.on_event(str)) #-200  8
    assertEqual(M.on_event(str), -200)  # 8

    str = json.dumps({"type": "ORDER_ACK", "order_id": 4, "time": "2017-03-15T10:15:10.976170"})
    #print(M.on_event(str)) #-200  9
    assertEqual(M.on_event(str), -200)  # 9

    str = json.dumps({"type": "CANCEL", "order_id": 3, "time": "2017-03-15T10:15:10.976431"})
    #print(M.on_event(str)) #-200  10
    assertEqual(M.on_event(str), -200)  # 10

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 5, "side": "SELL", "quantity": 900, "time": "2017-03-15T10:15:10.976536"})
    #print(M.on_event(str)) #-1100  11
    assertEqual(M.on_event(str), -1100)  # 11

    str = json.dumps({"type": "CANCEL_ACK", "order_id": 3, "time": "2017-03-15T10:15:10.976653"})
    #print(M.on_event(str)) #-400 12
    assertEqual(M.on_event(str), -400)  # 12

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 6, "side": "SELL", "quantity": 800, "time": "2017-03-15T10:15:10.976778"})
    #print(M.on_event(str)) #-1200 13
    assertEqual(M.on_event(str), -1200)  # 13

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 7, "side": "BUY", "quantity": 1700, "time": "2017-03-15T10:15:10.976893"})
    #print(M.on_event(str)) #-1200 14
    assertEqual(M.on_event(str), -1200)  # 14

    str = json.dumps({"type": "ORDER_ACK", "order_id": 5, "time": "2017-03-15T10:15:10.977002"})
    #print(M.on_event(str)) #-1200 15
    assertEqual(M.on_event(str), -1200)  # 15

    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 8, "side": "SELL", "quantity": 1300, "time": "2017-03-15T10:15:10.977103"})
    #print(M.on_event(str)) #-2500 16
    assertEqual(M.on_event(str), -2500)  # 16

    str = json.dumps({"type": "ORDER_ACK", "order_id": 6, "time": "2017-03-15T10:15:10.977206"})
    #print(M.on_event(str)) #-2500 17
    assertEqual(M.on_event(str), -2500)  # 17

    str = json.dumps({"type": "CANCEL", "order_id": 7, "time": "2017-03-15T10:15:10.977295"})
    #print(M.on_event(str)) #-2500 18
    assertEqual(M.on_event(str), -2500)  # 18

    str = json.dumps({"type": "ORDER_REJECT", "order_id": 7, "reason": "FIRM_RISK_LIMIT_EXCEEDED", "time": "2017-03-15T10:15:10.977395"})
    #print(M.on_event(str)) #-2500 19
    assertEqual(M.on_event(str), -2500)  # 19

    str = json.dumps({"type": "CANCEL", "order_id": 6, "time": "2017-03-15T10:15:10.977515"})
    #print(M.on_event(str)) #-2500 20
    assertEqual(M.on_event(str), -2500)  # 20

    str = json.dumps({"type": "ORDER_REJECT", "order_id": 8, "reason": "FIRM_RISK_LIMIT_EXCEEDED", "time": "2017-03-15T10:15:10.977665"})
    #print(M.on_event(str)) #-1200 21
    assertEqual(M.on_event(str), -1200)  # 21

    # my additional cases
    str = json.dumps({"type": "NEW", "symbol": "SPY", "order_id": 9, "side": "BUY", "quantity": 1000, "time": "2017-03-15T11:15:10.977103"})
    assertEqual(M.on_event(str), -1200)  # 22

    str = json.dumps({"type": "ORDER_ACK", "order_id": 9, "time": "2017-03-15T11:15:10.977206"})
    assertEqual(M.on_event(str), -1200)  # 23

    str = json.dumps({"type": "FILL", "order_id": 9, "filled_quantity": 200, "remaining_quantity": 700,
                      "time": "2017-03-15T11:15:10.975717"})
    assertEqual(M.on_event(str), -1000)  # 24

    str = json.dumps({"type": "FILL", "order_id": 9, "filled_quantity": 1000, "remaining_quantity": 0,
                      "time": "2017-03-15T11:15:10.975717"})
    assertEqual(M.on_event(str), -200)  # 25
