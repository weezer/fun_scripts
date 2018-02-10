import json
from collections import defaultdict

class MarkingPositionMonitor:
    def __init__(self):
        self.orders = {}
        self.markingPosition = defaultdict(int)

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
            self.markingPosition[symbol] += filled
        return self.markingPosition[symbol]