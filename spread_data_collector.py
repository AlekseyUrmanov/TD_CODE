import time

import tdamr_api as tdc
import spread_trade_fx
import requests




tdc = tdc.TDclient()





#Options_data = tdc.option_chain(details=['F', False])
#Options_data = tdc.sort_data_into_data_frames(Options_data)



# check spread, bid, ask
# track avg spread

# condition to remove order
# if ask is closer to our position than 50% of spread


# place bid order
# if not filled by the next loop cycle
# move it up.
# repeat

# place order at ask.
# if not filled by the next loop cycle
# move it down.
# repeat



# monitor spread process is started






class product:
    def __init__(self, shares, ticker):
        self.shares = shares
        self.ticker = ticker
        self.ask = 0
        self.bid = 0
        self.spreads = []
        self.open = False

    def spread(self):
        return self.bid - self.ask

    def process_data(self, data):
        self.bid = data[self.ticker]['bidPrice']
        self.ask = data[self.ticker]['askPrice']
        self.spreads.append(self.ask - self.bid)

    def avg_spread(self):

        return sum(self.spreads) / len(self.spreads)


def trade(product_object):

    if product_object.open:
        spread_trade_fx.sell_logic(product_object)

    else:
        spread_trade_fx.buy_logic(product_object)


products = ['CMG', 'NVDA', 'HD', 'LMT', 'CAT', 'NFLX']
cmg = product(10, 'CMG')


while True:

    data = tdc.get_quotes(details=[products, False])
    cmg.process_data(data)

    time.sleep(1)










