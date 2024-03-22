import matplotlib.pyplot as plt
import numpy as np
import time
import random
from XlsxTesting import TDclient

# covered call profit graph
# short straddle

class cc_graph:

    def __init__(self, premium, contract_strike, share_price, market_price, plot_name):
        self.premium = premium
        self.contract_strike = contract_strike
        self.share_price = share_price
        self.market_price = market_price
        self.plot_name = plot_name

    def make_graph(self):

        fig, ax = plt.subplots()

        max_profit = self.premium + (self.contract_strike - self.share_price) * 100
        zero_profit_share_price = self.share_price - (self.premium / 100)

        lower_x_axis = np.linspace(zero_profit_share_price * 0.98, zero_profit_share_price, 10)
        upper_x_axis = np.linspace(zero_profit_share_price, self.contract_strike, 10)
        upper_x_limit = np.linspace(self.contract_strike, self.contract_strike * 1.02, 10)
        flat_x_line = [max_profit for i in range(1, 11)]

        slope = (max_profit / (self.contract_strike - zero_profit_share_price))

        b = max_profit - (slope * self.contract_strike)

        y = slope * upper_x_axis + b
        ax.plot(upper_x_axis, y, 'green', lw=2)

        ax.plot(upper_x_limit, flat_x_line, 'green', lw=2)
        ax.text(zero_profit_share_price, 0 - 0.1 * max_profit, f'{round(zero_profit_share_price, 2)}', style='italic')
        ax.text(zero_profit_share_price, max_profit * 0.95, f'{round(max_profit, 2)}$')

        y = slope * lower_x_axis + b
        ax.plot(lower_x_axis, y, 'red', lw=2)

        ax.axhline(color='black', lw=1, alpha=0.2)
        ax.axvline(color='black', lw=1, alpha=0.2, x=zero_profit_share_price)
        ax.axhline(color='black', lw=1, alpha=0.2, y=max_profit)
        ax.axvline(color='black', linestyle='--', lw=1, alpha=1, x=self.market_price)
        ax.text(self.market_price, 0 - 0.2 * max_profit, f'{round(self.market_price, 2)}')

        plt.xlabel('Share Price')
        plt.ylabel('Profit or Loss at EXP')

        plt.ylim((slope * (zero_profit_share_price * 0.97) + b), max_profit * 1.1)

        fig.savefig(f"flask_dashboard/static/{self.plot_name}.png")

        plt.close()



tdc = TDclient()

while True:

    time.sleep(2)

    quote = tdc.get_quote(details=['SPY', False])
    print(quote)
    bid_quote = float(quote['SPY']['bidPrice'])
    ask_quote = quote['SPY']['askPrice']


    f = cc_graph(300, 12.5, 12.23, 12.23, 'plot_1')

    f.make_graph()














