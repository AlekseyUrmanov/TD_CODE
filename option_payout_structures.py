import matplotlib.pyplot as plt
import numpy as np


# covered call profit graph
# short straddle

share_price = 85.26
contract_price = 113
contract_strike = 86


def covered_call_graph(premium, contract_strike, share_price, market_price):
    # return profit loss array
    # return max profit
    # loss is reduced

    max_profit = premium + (contract_strike - share_price)*100
    zero_profit_share_price = share_price - (premium / 100)

    lower_x_axis = np.linspace(zero_profit_share_price * 0.98, zero_profit_share_price, 10)
    upper_x_axis = np.linspace(zero_profit_share_price, contract_strike, 10)
    upper_x_limit = np.linspace(contract_strike, contract_strike*1.02, 10)
    flat_x_line = [max_profit for i in range(1, 11)]


    slope = (max_profit / (contract_strike - zero_profit_share_price))

    b = max_profit - (slope * contract_strike)

    y = slope * upper_x_axis + b
    plt.plot(upper_x_axis, y, 'green', lw=2)

    plt.plot(upper_x_limit, flat_x_line, 'green', lw=2)
    plt.text(zero_profit_share_price, 0 - 0.1 * max_profit, f'{round(zero_profit_share_price, 2)}', style='italic')
    plt.text(zero_profit_share_price,  max_profit * 0.95, f'{round(max_profit, 2)}$')


    y = slope * lower_x_axis + b
    print(slope)
    plt.plot(lower_x_axis, y, 'red', lw=2)

    plt.axhline(color='black', lw=1, alpha=0.2)
    plt.axvline(color='black', lw=1, alpha=0.2, x=zero_profit_share_price)
    plt.axhline(color='black', lw=1, alpha=0.2, y=max_profit)
    plt.axvline(color='black', linestyle='--', lw=1, alpha=1, x=market_price)
    plt.text(market_price,  0 - 0.2*max_profit, f'{round(market_price, 2)}')




    plt.xlabel('Share Price')
    plt.ylabel('Profit or Loss at EXP')

    plt.ylim((slope * (zero_profit_share_price * 0.97) + b), max_profit*1.1)


    plt.show()


    return max_profit, zero_profit_share_price


covered_call_graph(113, 86, 84.26, 84.26)


