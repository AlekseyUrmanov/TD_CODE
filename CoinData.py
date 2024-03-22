import cbpro
import datetime
import time
import pandas as pd
from collections import OrderedDict
import numpy as np


def snap_to_book(data):

    order_book = {}

    asks = data['asks']
    bids = data['bids']

    for ask in asks:
        order_book[float(ask[0])] = ask[1]

    for bid in bids:
        order_book[float(bid[0])] = bid[1]

    return order_book


class MyWebsocketClient(cbpro.WebsocketClient):

    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'DOT-USD', 'XTZ-USD', 'RBN-USD']
        self.channels = ['matches', 'level2_50', 'ticker']
        self.auth = True
        self.api_key = '38ff39e7db27f252f45b41a943cdc505'
        self.api_passphrase = 'rb6ymq3638c'
        self.api_secret = 'amnDw3wrf08JsvsfSYar+KkS6OVYIwZ5c+gz4/CxyrS/dcQRvYcbwWpF3V93pgcA/xfPN/QSJlmQZXZBy8xAXg=='
        self.should_print = False
        self.stime = datetime.datetime.now()
        self.is_on = True

        print("--op--")

    def on_message(self, msg):

        try:
            pid = msg['product_id']

            if pid in obj.data:

                if msg['type'] == 'match':
                    side = msg['side']
                    size = msg['size']
                    if side == 'sell':
                        obj.data[pid]['diff'] = obj.data[pid]['diff'] + float(size)
                        if len(obj.data[pid]['arr']) > 1000:
                            obj.data[pid]['arr'].pop(0)
                        obj.data[pid]['arr'].append(obj.data[pid]['diff'])
                    else:
                        obj.data[pid]['diff'] = obj.data[pid]['diff'] - float(size)
                        if len(obj.data[pid]['arr']) > 1000:
                            obj.data[pid]['arr'].pop(0)
                        obj.data[pid]['arr'].append(obj.data[pid]['diff'])

                elif msg['type'] == 'snapshot':

                    order_book = snap_to_book(msg)
                    obj.data[pid]['book'] = order_book

                elif msg['type'] == 'l2update':

                    changes = msg['changes']
                    for change in changes:
                        if float(change[2]) == 0:
                            try:
                                del obj.data[pid]['book'][float(change[1])]
                            except KeyError:
                                pass
                        else:
                            obj.data[pid]['book'][float(change[1])] = change[2]
                elif msg['type'] == 'ticker':
                    bb = float(msg['best_bid'])
                    obj.data[pid]['best_bid'] = bb

            else:
                obj.data[pid] = {'diff': 0, 'arr': [], 'book': {}, 'best_bid': 0}
                obj.data[pid]['arr'].append(0)

        except KeyError as Exception:
            pass

    def on_close(self):
        print((datetime.datetime.now() - self.stime).seconds)
        self.is_on = False
        print("--cd--")


def auth():
    key = '38ff39e7db27f252f45b41a943cdc505'
    secret = 'amnDw3wrf08JsvsfSYar+KkS6OVYIwZ5c+gz4/CxyrS/dcQRvYcbwWpF3V93pgcA/xfPN/QSJlmQZXZBy8xAXg=='
    passphrase = 'rb6ymq3638c'

    auth_client = cbpro.AuthenticatedClient(key=key, b64secret=secret, passphrase=passphrase)
    pub_client = cbpro.PublicClient()

    return pub_client, auth_client


class CoinbaseData:
    def __init__(self, name):
        self.name = name
        self.data = {}

    def get_size_data(self, coin):

        try:
            big_data = self.data[coin]['arr']
        except KeyError:
            big_data = []
        return big_data

    @ staticmethod
    def get_nearest(arr, val):
        array = np.asarray(arr)
        idx = (np.abs(array - val)).argmin()
        return idx

    def get_book_df(self, coin):
        try:
            book_data = self.data[coin]['book']
            bid_price = self.data[coin]['best_bid']
        except KeyError:
            book_data = {}

        book_price_list = sorted(book_data)
        if len(book_price_list) == 0:
            df = pd.DataFrame()
            price_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            pass
        else:
            try:
                i = book_price_list.index(bid_price)
            except ValueError:
                i = self.get_nearest(book_price_list, bid_price)

            indexing_list = [i-4, i-3, i-2, i-1, i, i+1, i+2, i+3, i+4, i+5]
            price_list = []
            market_size_list = []

            #print(indexing_list)

            for index in indexing_list:
                if index < 0:
                    pass
                else:
                    try:
                        price_list.append(book_price_list[index])
                    except IndexError:
                        pass

            for price in price_list:
                try:
                    market_size_list.append(book_data[price])
                except KeyError:
                    pass

            price_list = price_list[::-1]
            market_size_list = market_size_list[::-1]

            if len(price_list) != len(market_size_list):
                if len(price_list) < len(market_size_list):
                    while len(price_list) != len(market_size_list):
                        price_list.append(0)
                else:
                    while len(price_list) != len(market_size_list):
                        market_size_list.append('0')

            df_data = OrderedDict(
                [
                    (f'Market Size {coin}', market_size_list),
                    ('Price', price_list)
                ]
            )
            df = pd.DataFrame(df_data)

        return df, price_list[5], price_list[4]


wbs = MyWebsocketClient()
obj = CoinbaseData('Streamer')

'''
try:
    wbs.start()
    while True:
        time.sleep(1)
        b, a = obj.get_bid_ask('BTC-USD')
        print(a)
        print(b)
finally:

    wbs.close()

'''