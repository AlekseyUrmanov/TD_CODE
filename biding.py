import time

import tdamr_api as TDC
import requests
'''
pull options chain
find least bids below intrinsic
place bid
poll the bid price
adjust quote
'''


stocks = ['F']

tdc = TDC.TDclient()




def option_bid_filter(stock):

    data_raw = tdc.option_chain(details=[stock, False])
    data = tdc.sort_data_into_data_frames(data_raw)

    # Take the nearest option chain because contracts have the least amount of built-in premium
    near_put_chain = data[1]

    exp_dates = near_put_chain.keys()

    for date in exp_dates:

        subset_put_chain = near_put_chain[date][['bid', 'intrinsicValue', 'totalVolume', 'symbol']]
        subset_put_chain = subset_put_chain[subset_put_chain['totalVolume'] > 0]
        subset_put_chain = subset_put_chain[subset_put_chain['bid'] < subset_put_chain['intrinsicValue']]
        if len(subset_put_chain):
            print(subset_put_chain)


'''
for i in stocks:
    option_bid_filter(i)
'''
'''
class hold_order_at_bid_clx(TDC):
    def __init__(self, order_price, symbol, quant):
        self.open = False
        self.quant = quant
        self.order_price = order_price
        self.symbol = symbol
        self.order_id = None
        self.tdc = None

    def start(self):
        self.tdc = TDC.TDclient()

        self.tdc.option_order(instruction='BUY_TO_OPEN',
                              symbol=self.symbol,
                              price=self.order_price,
                              quantity=self.quant)

        get_orders_data = self.tdc.get_account_data()
        oid = get_orders_data[0]['orderId']
        self.order_id = oid
        self.open = True
        self.hold_at_bid()

    def hold_at_bid(self):

        if self.open:
            #bid_price_quote = self.tdc.
            pass

'''





def service_position(position):

    # given position, maintain it

    # pol the curreent bid
    # if quote > bid and < intrinsic : Maintain
    # if quote > bid and > intrinsic : Move below intrinsic (check if bid < intrinsic, move to bid)
    # if quote < bid and > intrinsic : Remove order
    # if quote < bid and < intrinsic : Move to bid (Move order up, if bid is below intrinsic)
    current_bid = 1.13
    current_intrinsic = 1.16
    if position.quote_price > ((current_bid*100) - 1.3):
        if position.quote_price < ((current_intrinsic*100) - 1.3):
            # Maintain
            pass
        else:
            # Move below intrinsic (check if bid < intrinsic, move to bid)
            pass
    else:
        if position.quote_price < ((current_intrinsic * 100) - 1.3):
            # Move to bid (Move order up, if bid is below intrinsic)
            pass
        else:
            # Remove order
            pass




def match_OID(order_details):


    headers = {
        'Authorization': 'Bearer 409vPN5L90l59UhEQccojnfo9BGPC82gjTyCi4MKmEy+rEpnRJ0kzBAIVhXpzXweujIFUz4jzNNOocNnF2Ic8DoNY/m7Q5kWhyUmliWmByCT5GNF/KjwvIh1gRlI/aujp1DeiYYO2ag0Vzhmw/Lj/DfpjNrp3SaQBV79a2gtSvAQbeRwGncZXRebb0D6er3seVTBTI/OiyORgn9H7LpObHS1HJPlZkmTzt8joRHKG1S2DLHYGdMdcdIejK8RWsQJ1o+zE2MhLfgxghBli6hfMyojvEtW0HaJU433p+mEMPQqPsh0ytmLHxyI/3O46BdvhGrZa4bv1yp5ZMbj3MD6B6HcWpGsfzz5HDLEHAMeGRrMvd28FmNrcndZpNl8bvFExDpjal2Oe9qGvqryIPWOWNGFOuZddXmj8nbUTnZPE8GYjW02PJHJTMc+lcLWPeDEvF4TPuXlzA7y1oLl8ktJxisaEdLWb0vyJ5Eir/zeMOwc52ekNaVrNEI6tgkPaMcZQoHDfc//nIb7WBPIbihD7THosWNOx1QSamE4mc3RuFOB9JLqWno1UEA1zVI100MQuG4LYrgoVi/JHHvlhzqOvkYlL86rg0yZ5bB/y/userwadkYgobKDRYC2BDKwcAUzGqJHxP9jxYlG/yi65MdXjvmPoijl1EiZMm6gAYNKQMGOUB+JcQRcoVeK44XHdjigqYdlks3ywHjChNzq9gOPme1Gs/GU1yRKtDUcVvJAWHBctush1PGm5B1KqqkD+9cCIMli5FDpup8Rh63OiN3oaDqEjXT8jMBpXAzgoHS0jZ5lCzb0G0MkYU414rTWJEMnrBdVHCLXbmRA+0Nq5bbg0pdISkfwli2r/c4mfBuKvNdQ7PnNef1z2TjFKdQ7xj64teybEBEU6s9UpR9OkN8sWKDMzS/JVOCzwoYymSrQvYcmCMZHQ+VJS1aOGe0ZO+JjkaopVVdWEdOq2MN3aFaFQd32Ltfg7u++oWg++O3EoXErCvX3ghxKzHi5rKMNaR/VhzVvlz4pF/QGzGAAXV/uOafEDhciPUwF0VdoaA65/x8+bDAKjfWDMgywTPym9Hy8vExz99H4ozDUATXPHd5jK9g+jURza0V2GL1ITg0kh0YMLHZYik95n8oajfT9U3yaeLj7Q0f9QvI=212FD3x19z9sWBHDJACbC00B75E',
    }

    params = {
        'status': 'PENDING_ACTIVATION',
    }

    response = requests.get('https://api.tdameritrade.com/v1/accounts/236642469/orders', params=params, headers=headers)
    print(response)

    pass





order_dic = {}

sym = 'F_012624P12'




rtq_data = tdc.specific_option_chain_quote(symbol=sym, real_time=True)

bid_qp = rtq_data['option']['bid']


order = tdc.option_order(instruction='BUY_TO_OPEN', symbol=sym, price=bid_qp, quantity=1)
#print(order)

d = tdc.get_account_data()
OOID = d[0]['orderId']
price = d[0]['price']

order_dic[OOID] = {'price':bid_qp, 'symbol':sym}


while True:
    rtq_data = tdc.specific_option_chain_quote(symbol=sym, real_time=True)

    removeable = []
    new_ordrs = []

    def new_order(p):
        order = tdc.option_order(instruction='BUY_TO_OPEN', symbol=sym, price=p, quantity=1)
        d = tdc.get_account_data()
        OOID = d[0]['orderId']
        price = d[0]['price']

        order_dic[OOID] = {'price': price, 'symbol': sym}


    for i in order_dic:
        if order_dic[i]['price'] == rtq_data['option']['bid']:
            pass
        elif float(order_dic[i]['price']) >= (float(rtq_data['option']['ask']) - 0.013):
            print('PRICE TOO HIGH')
            tdc.cancel_option_order(OID=i)
            removeable.append(i)
            rtq_data = tdc.specific_option_chain_quote(symbol=sym, real_time=True)
            new_ordrs.append(rtq_data['option']['bid'])

        else:
            print('PRICE TOO LOW')
            tdc.cancel_option_order(OID=i)
            removeable.append(i)
            rtq_data = tdc.specific_option_chain_quote(symbol=sym, real_time=True)
            new_ordrs.append(rtq_data['option']['bid'])

    for i in new_ordrs:
        new_order(i)

    if removeable:
        for i in removeable:
            del order_dic[i]


    time.sleep(10)









#"accountId": 236642469
#12569169652

# KEYS : orderId, quantity, price

# array of dictionaries, to get order id do order ID, for info subset ['orderLegCollection'], or pull quantity and price.


