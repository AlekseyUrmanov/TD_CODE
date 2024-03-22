from XlsxTesting import TDclient
import time
import threading
import datetime
import matplotlib.pyplot as plt
import math as m
import json

tdc = TDclient()


product = 'SPY'
odate = '2023-03-10'
price = '392.0'
start_time = str(datetime.datetime.now())


def dg_hedge(product, odate, price):
    tdc = TDclient()

    # ci (s,o) v = change in share or option value across periods

    option_stats = {'bid':[], 'ask':[], 'delta':[], 'gamma':[]}
    equity_stats = {'bidPrice':[], 'askPrice':[]}
    hedge_stats = {'shares':[], 'share_value':[], 'share_pl':[]}

    def gather_data():

        raw_option_chain_data = tdc.option_chain(details=[product, True])
        clean_option_chain_data = tdc.sort_data_into_data_frames(raw_option_chain_data)
        clean_option_chain_data = clean_option_chain_data[0][odate]

        print(clean_option_chain_data[['bid', 'ask', 'delta']])
        for label in option_stats:
            option_stats[label].append(clean_option_chain_data[label].loc[price])

        equity_realtime_quote = tdc.get_quote(details=[product, True])

        for label in equity_stats:
            equity_stats[label].append(equity_realtime_quote[product][label])

        hedge_stats['shares'].append(int(float(option_stats['delta'][-1])*100))
        hedge_stats['share_value'].append(hedge_stats['shares'][-1] * float(equity_stats['bidPrice'][-1]))
        try:

            hedge_stats['share_pl'].append((float(equity_realtime_quote[product]['bidPrice'])
                                            -float(equity_stats['bidPrice'][-2]))
                                           * (hedge_stats['shares'][-2])) # -1 or -2
        except IndexError:
            hedge_stats['share_pl'].append(0)

    def show_hedge_stats():
        print(f'Option value change : {round(((option_stats["bid"][0] - option_stats["bid"][-1])*100),4)}')
        print(f'Share PL : {round((sum(hedge_stats["share_pl"])), 4)}')
        print(f'Shares outstanding : {hedge_stats["shares"][-1]}')
        pass

    try:
        while True:
            gather_data()
            show_hedge_stats()
            time.sleep(30)
    finally:
        show_hedge_stats()

        end_time = str(datetime.datetime.now().hour)
        product_data = {'equity_data': equity_stats, 'derivative_data': option_stats, 'hedge_data': hedge_stats}
        json_object = json.dumps(product_data, indent=4)

        print(product_data)

        file_name = product +'_'+ price +'_'+ odate
        with open(f"total_hedging_json_data/{file_name}.json", "w") as outfile:
            outfile.write(json_object)


dg_hedge(product, odate, price)



'''
with open("total_hedging_json_data/SPY402.02023-03-0315.json", "r+") as outfile:
    json_data = outfile.read()

hedge_data = eval(json_data)
'''