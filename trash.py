import requests
import main
from tdamr_api import TDclient
import time



tdc = TDclient()

# this is the ex date
date = "2024-02-15"

div_date_data_raw = main.snc(date)
div_date_data = main.sort_data(div_date_data_raw)

put_chain = {}

for stock in div_date_data.keys():

    # only quarterly dividends don't have strike contract adjustments
    if float(div_date_data[stock]['cash']) * 4 != float(div_date_data[stock]['yearly_cash']):
        pass
    else:
        data_raw = tdc.option_chain(details=[stock, False])
        data = tdc.sort_data_into_data_frames(data_raw)

        # Take the nearest option chain because contracts have the least amount of built-in premium
        data
        near_put_chain = data[1]

        # Filter out empty option chains
        if data[1]:
            single_chain = data[1][data[1].keys()[0]]
            '''#[u'ask', u'askSize', u'bid', u'bidAskSize', u'bidSize', u'closePrice',
       u'daysToExpiration', u'deliverableNote', u'delta', u'description',
       u'exchangeName', u'expirationDate', u'expirationType', u'gamma',
       u'highPrice', u'inTheMoney', u'intrinsicValue', u'isIndexOption',
       u'last', u'lastSize', u'lastTradingDay', u'lowPrice', u'mark',
       u'markChange', u'markPercentChange', u'mini', u'multiplier',
       u'netChange', u'nonStandard', u'openInterest', u'openPrice',
       u'optionDeliverablesList', u'pennyPilot', u'percentChange', u'putCall',
       u'quoteTimeInLong', u'rho', u'settlementType', u'strikePrice',
       u'symbol', u'theoreticalOptionValue', u'theoreticalVolatility',
       u'theta', u'timeValue', u'totalVolume', u'tradeDate',
       u'tradeTimeInLong', u'vega', u'volatility'],
      dtype='object')''' # keys of option chain
            single_chain = single_chain[['bid', 'ask', 'intrinsicValue', 'totalVolume']]
            print(sum(single_chain["totalVolume"]))
            single_chain["threshold"] = single_chain['intrinsicValue'] + float(div_date_data[stock]['cash'])
            single_chain["profit"] = (single_chain["threshold"] - single_chain["ask"]) * 100
            single_chain['spread'] = single_chain['ask'] - single_chain['bid']

            single_chain = single_chain[single_chain['intrinsicValue']>=0]


            put_chain[stock] = single_chain


        else:
            print('No Option Chain')
            pass


for stock in put_chain.keys():

    print("{} {}$/share".format(stock, div_date_data[stock]['cash']))
    print(put_chain[stock])
















# database with dates of all upccoming div's for nxt 10 days

# analyze all options chains for these tickers, display profitable instances.


















