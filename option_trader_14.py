from XlsxTesting import TDclient
import time
import datetime


class optionCCtrade(TDclient):

    def __init__(self, product):
        super().__init__()
        self.product = product
        self.market_open = False
        self.closing_price = None
        self.position = False
        self.contract_position = [] # strike, expiration, type

        self.accumulated_premium = 0

    @staticmethod
    def get_time():
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        # print(hour)
        # print(minute)
        # 9, 30 open
        # 16, 0 close
        return [hour, minute]

    @staticmethod
    def get_day_date():
        day = str(datetime.datetime.now().date())
        return day

    def set_vars(self):
        hr, mn = self.get_time()
        weekend_check = datetime.datetime.now().isoweekday()
        if weekend_check == 6 or weekend_check == 7:
            self.market_open = False
        else:
            if hr == 9 and mn >= 40:
                self.market_open = True
                self.new_access_token()
            elif hr < 16:
                self.market_open = True
                self.new_access_token()
            else:
                if self.market_open:
                    self.market_open = False
                    self.closing_price = self.get_quote(details=[self.product, True])
                    self.closing_price = float(self.closing_price[self.product]['bidPrice'])

                else:
                    pass

    def product_market_price(self):
        quote = self.get_quote(details=[self.product, True])
        quote = float(quote[self.product]['bidPrice'])
        return quote

    def get_atm_option_info(self):

        spy_quote = self.product_market_price()

        spy_option_data = self.option_chain(details=[self.product, True])
        spy_df = self.sort_data_into_data_frames(spy_option_data)
        spy_call_chain, spy_put_chain = spy_df[0], spy_df[1]

        today_day = self.get_day_date()

        expiration_chain = spy_call_chain[today_day]

        for price in list(expiration_chain.index):
            if float(spy_quote) > float(price):
                pass
            else:
                atm_price = price
                break

        atm_option_data = expiration_chain.loc[[str(atm_price)]]
        strike = atm_price

        option_bid_price = float(atm_option_data['bid'])
        return option_bid_price, strike

    def expired_position(self):
        expiration_date = self.contract_position[1]
        today_date = self.get_day_date()
        if expiration_date == today_date:
            return False
        else:
            return True

    def close_position(self):

        contract_price = float(self.contract_position[0])

        today_date = self.get_day_date()
        self.position = False

        if contract_price > self.closing_price:
            print('option expired otm || ' + today_date)
            print(f'share value is {100*self.product_market_price()}\n')
        else:
            print('option expired itm || ' + today_date)
            print(f'shares sold at {contract_price}\n')
        self.contract_position = []

    def create_position(self):

        quote = self.product_market_price()

        product_bid_price, strike = self.get_atm_option_info()
        today_date = self.get_day_date()

        self.position = True
        print(f'Bought 100 shares at {quote}')
        print(f'Sold {strike} {today_date} call @ {product_bid_price}\n')
        self.contract_position = [strike, today_date, 'sold_call']

        self.accumulated_premium += float(product_bid_price)

    def run(self):
        while True:
            self.set_vars()
            if self.market_open:
                if self.position:
                    if self.expired_position():
                        self.close_position()
                    else:
                        pass
                else:
                    self.create_position()
            else:
                print('Market closed')
                pass
            time.sleep(60)



occ = optionCCtrade('SPY') # QQQ, DIA

occ.run()
