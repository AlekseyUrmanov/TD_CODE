import json

import db_manager
import main
from tdamr_api import TDclient
import time


def create_div_date_data(date):
    db_op = db_manager.div_db_operator('divDB')

    tdc = TDclient()

    #date = "2023-12-29"

    tableName = 'date_'+ date.replace('-', '')
    db_op.create_table(tableName)


    div_date_data_raw = main.snc(date)
    div_date_data = main.sort_data(div_date_data_raw)


    for stock in div_date_data.keys():

        # only quarterly dividends don't have strike contract adjustments
        if float(div_date_data[stock]['cash']) * 4 != float(div_date_data[stock]['yearly_cash']):
            pass
            print('passed')
        else:
            data_raw = tdc.option_chain(details=[stock, False])
            db_op.add_data(data_raw, stock, tableName, div_date_data[stock]['cash'])
            print('done')



def min_spread(date):
    tdc = TDclient()
    db_op = db_manager.div_db_operator('divDB')


    tableName = 'date_' + date.replace('-', '')
    stock_ochain_datas = db_op.pull_data(table_name=tableName)

    for row in stock_ochain_datas:

        put_chain = {}

        data_raw = eval(row[1]) # [1] bc returns every col with index

        data = tdc.sort_data_into_data_frames(data_raw)
        stock = data_raw['stock']
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
      dtype='object')'''  # keys of option chain
            single_chain = single_chain[['bid', 'ask', 'intrinsicValue', 'totalVolume']]
            print(sum(single_chain["totalVolume"]))
            single_chain["threshold"] = single_chain['intrinsicValue'] + float(data_raw['cash'])
            single_chain["profit"] = (single_chain["threshold"] - single_chain["ask"]) * 100
            single_chain['spread'] = single_chain['ask'] - single_chain['bid']
            put_chain[stock] = single_chain



create_div_date_data('2023-12-29')
min_spread('2023-12-29')



