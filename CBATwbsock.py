
from __future__ import print_function
import json
import base64
import hmac
import hashlib
import time
from threading import Thread
from websocket import create_connection, WebSocketConnectionClosedException


class WebsocketClient(object):
    def __init__(
            self,
            url="wss://advanced-trade-ws.coinbase.com",
            products=None,
            message_type="subscribe",
            mongo_collection=None,
            should_print=True,
            auth=False,
            api_key="",
            api_secret="",
            api_passphrase="",
            # Make channels a required keyword-only argument; see pep3102
            *,
            # Channel options: ['ticker', 'user', 'matches', 'level2', 'full']
            channels):
        self.url = url
        self.products = products
        self.channels = channels
        self.type = message_type
        self.stop = True
        self.error = None
        self.ws = None
        self.thread = None
        self.auth = auth
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase
        self.should_print = should_print
        self.mongo_collection = mongo_collection
        self.secret_key = 'viwih1ugG3gclxhma6XM55RY2KfqCk25'
        self.access_key = 'AJ14jFXUZwB9gLvv'


    def start(self):
        def _go():
            self._connect()
            self._listen()
            self._disconnect()

        self.stop = False
        self.on_open()
        self.thread = Thread(target=_go)
        self.keepalive = Thread(target=self._keepalive)
        self.thread.start()

    def get_auth_sig(self, **kwargs):

        timestamp = str(int(time.time()))
        message = timestamp + kwargs['channel'] + kwargs['product']

        signature = hmac.new(self.secret_key.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()
        return signature.hex()

    def _connect(self):

        timestamp = str(time.time())

        hmac_sig = self.get_auth_sig(channel=self.channels, product=self.products)


        sub_params = {
            "type": "subscribe",
            "product_ids": [
                "AVT-USD",
            ],
            "channel": "level2",
            "api_key": 'AJ14jFXUZwB9gLvv',
            "timestamp": "1660838876",
            "signature": "jd83jdhsus83krkfjf883jkjnsjdu84j3nd8dj3",
        }

        self.ws = create_connection(self.url)

        self.ws.send(json.dumps(sub_params))

    def _keepalive(self, interval=30):
        while self.ws.connected:
            self.ws.ping("keepalive")
            time.sleep(interval)

    def _listen(self):
        self.keepalive.start()
        while not self.stop:
            try:
                data = self.ws.recv()
                msg = json.loads(data)
            except ValueError as e:
                self.on_error(e)
            except Exception as e:
                self.on_error(e)
            else:
                self.on_message(msg)

    def _disconnect(self):
        try:
            if self.ws:
                self.ws.close()
        except WebSocketConnectionClosedException as e:
            pass
        finally:
            self.keepalive.join()

        self.on_close()

    def close(self):
        self.stop = True   # will only disconnect after next msg recv
        self._disconnect() # force disconnect so threads can join
        self.thread.join()

    def on_open(self):
        if self.should_print:
            print("-- Subscribed! --\n")

    def on_close(self):
        if self.should_print:
            print("\n-- Socket Closed --")

    def on_message(self, msg):
        if self.should_print:
            print(msg)
        if self.mongo_collection:  # dump JSON to given mongo collection
            self.mongo_collection.insert_one(msg)

    def on_error(self, e, data=None):
        self.error = e
        self.stop = True
        print('{} - data: {}'.format(e, data))


class MyWebsocketClient(WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["BTC-USD", "ETH-USD"]
        self.message_count = 0
        print("Let's count the messages!")

    def on_message(self, msg):
        print(json.dumps(msg, indent=4, sort_keys=True))
        self.message_count += 1

    def on_close(self):
        print("-- Goodbye! --")



def get_auth_sig(**kwargs):
    timestamp = str(int(time.time()))
    message = timestamp + kwargs['channel'] + kwargs['product']
    secret_key = 'viwih1ugG3gclxhma6XM55RY2KfqCk25'

    signature = hmac.new(secret_key.encode('utf-8'), message.encode('utf-8'),
                         digestmod=hashlib.sha256).digest()
    return signature.hex()


sig = get_auth_sig(channel='level2', product='AVT-USD')
print(sig)

