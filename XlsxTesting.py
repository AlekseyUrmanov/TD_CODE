import json

import requests
import pandas as pd

import testing
import datetime
import time


class TDclient:

    def __init__(self):
        self.data_base = testing.KeyConnection()

        self.ck = "Y1KS0BMRKRBSI6CVNYIHHN1NVF3VUI2J"
        self.at = "Bearer 9SOucL/ARpXwgP+ASLj9baBJvkewc22drn/nCQ1fmXz7Jb6cx+3LNtZtAiR/LJApDctIFSub6Fr9FbnrrQQIgI8aOViS62ZnxVbop+0FkDGAAExRilbmQu82piumwM4QudDwITCaflZbnwcHKEn8gMidErrz5mQMBE9CHnepeDhVmfeh0b0r4SMRJO8ju5Gv3xpI/1Gfwmr9fFs+H0lH+sXfr4ivB3aKgUOylaJjHMlh9xGZfkRksP5TiBE2w6TuW+pVOb79uHM7Scrg6p99BQIjJyJD7A9QeoZHztAMxiq712epY1TSp90Jbc+x0tErVV5d5fHAe+FJ2nW/mpItAzHcs7weFLekBUVypx0lVWZM4ZdcDpjiTbkYOUGtrHGc53iprYgKaBk6CiPaG1kUkFUzZAwl2CB2XfiqbuNOttoVm09SlFuK21nb2/q0V0D4NCy3wpDlG0xvqfOzTd6m2IvyoxnF+pduR6allHCCul5vggSPewhIJP39RCDqzmsCodzRkOR8oodpCxEaeYZ4sjCIGg/jyJZTJp/cGx/yCWkQKHaRJqBPKHLsml1100MQuG4LYrgoVi/JHHvl7ZtuDDIMUcLWqEQmaFO2xoIpzaOGaOALLvQBLYIAXov+Adf4U7z3gUCtysnG+PZdnTKoaCdN3Swu/J0Ak/4e7GojmbqZ7o2/z+8Bj0LQPd3XfLQmzeLmmNDgjGiS1X++4hQrOJL5h9bRigSDpM4npDYGXLkhB1P3GlMM4u4Y6Eg8mnUvn/zVpxm2hCYGkGi3WtGDwmwXw7efJTmnaZkXmuyNQ+iE2BZVO/3AP2d3Y59Obnd5kBdxu9AZjAX+12+z4rAyBot+ldvBPcrpIMQ2eTlUcVE6czLBZDyYwXN+YxrekMVr7lWTmY41wrp2+WVwKjDw8jBDSeHpYUPhgJCIV+YAdL7wdFGf0CizNfZwpKMgaE1/MQkx52aYnZ+OOEN8VnEofWI4VgLwR/j0pRaTA33iVX8nU4kVH0P7ynk9iNbDg9P1Ghbdyb5l1f9uhEhVqihysUBexZrI7aGIFxctmigLMsGMGXj63FvMfb6m2hqF83UMAREjObFHlxLtzxnpzQLDGNrc96RA5e2+TObgNLYAKu9cjiGehG86j/jux6/bEk63LDqz9LknLBA=212FD3x19z9sWBHDJACbC00B75E"
        self.rt = "Y6shAZ5BYmvqCIgsqCjgfgNjKD60Kd/EexOtPaBjtJk3OAlaDv6U5RCv853Km8enQasAUJghXB4P7nObIwxb/0Gtaah8Gu8myWbHllN8o3uqiK/REcWbcnaNh/ybjesLVZ4QGXIFoX+S30AAk7ft23efTWt02tLiQiM1BY2SLudtVKp9kAln4W2Hjn4U527oamp+o2NHyC23uuxrAxYypr2dTFxMiZFbLKC+41EFwsxdamJvslvuGsiB1Oxyn/7ZrLa85aox4OGtIbvZpUbbSIJ8HYld4aMflIsPqtT5H8UN9IkHi1BKPzf1ieg6hFT5d/8dnx+YU5iUzOx6/IIJ06KOjp1AWbamc4/mAgy5lgpHcMOdSltaKU+SvZZ9LY8dIdlqLzf+1I8ZWnVf3Vimc2VfRPGFBhc5Fi8V0t03xNALfA23mV1+1OuLv+k100MQuG4LYrgoVi/JHHvlQiRiinShyQDtZdRQuxoJPdEXcq5trHXpyhoVrYndh/wbZy0ER0Sy5prVLh7K/Ey6akhDlWlTvynXk0LdDYhWgvPtynSSuxQ7/hHByeZD9hJ/3Gl9dDuBrc63Atl8/rr7Si65XnP39FS1hzKUVAb7qTMqIGbga60ntwsB+n6+8g3v/oMzvoTLTlU1MBC8lOcC8xYAxmDjR+midbF11B/fgMSJsaxcUKDzacX1ibIgJEfdwjl4C4ARBwDGjC8uuO4KTNliHNirnKdH6Cl+xHpADGmPBfmhgBlFvE3YrMy3NH4GBR2bhYfZpoMTUe0z2r7RfYNxvqWjqB+Fypv01TVBi0/lLo8o0qhhaYHg4765y+Qn3K7CgYx4BO53A7r5iJK+buWSGa7liVsjC/hYTlMWq7SVI/4g8dTCgOtWSCweJbOuBGWuBQGkF8hx7zM=212FD3x19z9sWBHDJACbC00B75E"
        #self.new_access_token()

    def get_fundamentals(self, symbol):

        # url for specific call of data
        url = 'https://api.tdameritrade.com/v1/instruments'
        # format tickr inserts the stock ticker variable, r is raw string.

        payload = {'apikey': self.ck,  # Simple payload structuring
                   'symbol': symbol,
                   'projection': 'fundamental'
                   }

        response = requests.get(url=url, params=payload)
        content = self.response_processing(response, self.get_fundamentals, symbol)
        fund_data = (content[symbol])['fundamental']
        return fund_data

    def get_account_data(self, details='orders'):
    # orders or positiions
        # url for specific call of data
        url = 'https://api.tdameritrade.com/v1/accounts/236642469'
        # format tickr inserts the stock ticker variable, r is raw string.
        headers = {
            'Authorization': self.at
        }

        params = {
            'fields': details,
        }

        response = requests.get('https://api.tdameritrade.com/v1/accounts/236642469', params=params, headers=headers)
        content = self.response_processing(response, self.get_account_data, details)
        return content

    def get_quote(self, details=[]):

        symbol = details[0]
        real_time = details[1]

        # with authentication there will be real_time_data entitled : true
        url = format('https://api.tdameritrade.com/v1/marketdata/{}/quotes', symbol)

        if real_time:
            params = {
                'apikey': self.ck,
            }
            header = {
                'Authorization': self.at,
                'Content-Type': 'application/json'
            }
            print('tried real time')
        else:
            params = {
                'apikey': self.ck,

            }
            header = {}

        response = requests.get(url=url, params=params, headers=header)
        content = self.response_processing(response, self.get_quote, symbol)
        return content

    def get_limit_order_book(self, ticker):
        endpoint = f"https://api.tdameritrade.com/v1/marketdata/{ticker}/orderbook"

        headers = {
            'apikey': self.ck,
            'Authorization': self.at
        }

        response = requests.get(url=endpoint, headers=headers)
        print(response)
        print(response.status_code)
        #content = self.response_processing(response, self.get_limit_order_book, ticker)
        print(json.loads(response.content))
        z = json.loads(response.content)
        print(z)

        content = response.json()
        return content

    def option_chain(self, details=[]):

        ticker = details[0]
        real_time = details[1]
        if real_time:

            params = {
                'apikey': self.ck,
                'symbol': ticker,
                'contractType': 'ALL',
                'strikeCount': '14',
                'includeQuotes': 'FALSE',
                'strategy': 'SINGLE',
            }
            header = {
                'Authorization': self.at,
                'Content-Type': 'application/json'
            }
            print('tried real time')

        else:

            params = {
                'apikey': self.ck,
                'symbol': ticker,
                'contractType': 'ALL',
                'strikeCount': '10',
                'includeQuotes': 'FALSE',
                'strategy': 'SINGLE',
            }

            header = {}

        response = requests.get('https://api.tdameritrade.com/v1/marketdata/chains', params=params, headers=header)
        content = self.response_processing(response, self.option_chain, details)
        return content

    @staticmethod
    def sort_data_into_data_frames(raw_json):

        all_frames = []

        for key in ['callExpDateMap', 'putExpDateMap']:
            call_or_put_data = raw_json[key]
            expiration_date_list = list(call_or_put_data.keys())

            framed_option_chain = {}
            for date in expiration_date_list:

                strikes = list((call_or_put_data[date]).keys())
                expire_data_relative_data = []

                for strike in strikes:
                    strike_data_dict = (call_or_put_data[date][strike])[0]
                    expire_data_relative_data.append(strike_data_dict)

                frame = pd.DataFrame.from_records(expire_data_relative_data, index=strikes)
                index_date = (date.split(':'))[0]
                # date string from TD comes as date:value, we just grab the date
                framed_option_chain[index_date] = frame

            all_frames.append(framed_option_chain)

        return all_frames
        # frames is a list, 2 entries of dictionaries, first is a dictionary of call data frames, where the keys are
        # the dates, second entry is the put dictionary of data frames.

    def market_order(self, details=[]):

        # string, int, string
        bos = details[0]
        quantity = details[1]
        ticker = details[2]

        url = 'https://api.tdameritrade.com/v1/accounts/236642469/orders'

        headers = {
            'Authorization': self.at,
            'Content-Type': 'application/json',
        }

        data = {"orderType": "MARKET",
               "session": "NORMAL",
               "duration": "DAY",
               "orderStrategyType": "SINGLE",
               "orderLegCollection": [{"instruction": f"{bos}", "quantity": quantity,
               "instrument": {"symbol": f"{ticker}", "assetType": "EQUITY"}}]}

        response = requests.post(url=url, headers=headers,
                                 data=json.dumps(data))
        content = self.response_processing(response, self.market_order, details)

    def limit_order(self, details=[]):

        bos = details[0]
        quantity = details[1]
        ticker = details[2]
        price = details[3]

        url = 'https://api.tdameritrade.com/v1/accounts/236642469/orders'

        headers = {
            'Authorization': self.at,
            'Content-Type': 'application/json',
        }

        data = {"orderType": "LIMIT",
               "session": "NORMAL",
               "duration": "DAY",
               "price": f'{price}',
               "orderStrategyType": "SINGLE",
               "orderLegCollection": [{"instruction": f"{bos}", "quantity": quantity,
               "instrument": {"symbol": f"{ticker}", "assetType": "EQUITY"}}]}

        response = requests.post(url=url, headers=headers,
                                 data=json.dumps(data))
        content = self.response_processing(response, self.limit_order, details)

    def option_order(self, **kwargs):

        details = kwargs

        url = 'https://api.tdameritrade.com/v1/accounts/236642469/orders'

        headers = {
            'Authorization': self.at,
            'Content-Type': 'application/json',
        }

        # BUY_TO_OPEN  BUY_TO_CLOSE  SELL_TO_OPEN  SELL_TO_CLOSE
        # symbol is option/strike/date specific, get from data frame
        data = {
                "complexOrderStrategyType": "NONE",
                "orderType": "LIMIT",
                "session": "NORMAL",
                "price": details['price'],
                "duration": "DAY",
                "orderStrategyType": "SINGLE",
                "orderLegCollection": [
                    {
                      "instruction": details['instruction'],
                      "quantity": details['quantity'],
                      "instrument": {
                        "symbol": details['symbol'],
                        "assetType": "OPTION"
                        }
                    }
                  ]
                }

        response = requests.post(url=url, headers=headers,
                                 data=json.dumps(data))
        self.response_processing(response, self.option_order, details)

    def new_access_token(self):

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'grant_type': 'refresh_token',
            'refresh_token': self.rt,
            'access_type': '',
            'code': '',
            'client_id': self.ck,
            'redirect_uri': ''
        }

        response = requests.post('https://api.tdameritrade.com/v1/oauth2/token', data=data)
        content = self.response_processing(response, self.new_access_token, None)
        new_access_token = content['access_token']
        full_code = 'Bearer ' + new_access_token
        self.data_base.replace_at(full_code)
        self.at = full_code

    def cancel_order(self, order_num):

        url = f'https://api.tdameritrade.com/v1/accounts/236642469/orders/{order_num}'

        headers = {
            'Authorization': self.at
        }

        response = requests.delete(url=url,
                                   headers=headers)
        print(response)
        response_code = response.status_code

    def _generate_position(self, params):
        pass

    def response_processing(self, response, func_call, parameters):
        #show sresponses that came, update tokens and variables, recall operations, keep operation log
        print(f'\n{func_call.__name__.upper()} RESULTS')
        response_code = response.status_code
        print(f'Response : <{response_code}>')

        if response_code == 401:
            self.new_access_token()
            print('Created New Access Token')
            print('Updated Token')
            print('Running Correction Instance')
            if type(parameters) == dict:
                data = func_call(**parameters)
            else:
                data = func_call(details=parameters)
            print('Instance Complete')
            return data

            # run process again

        elif response_code == 200 or response_code == 201:
            try:
                print(f'Call Details : {parameters}')
                content = response.json()
                print('Returning Data')
                print('Call Complete')
                return content
            except Exception:
                print('No data to return')
                print('Call Complete')
                return

        elif response_code == 400: # should not occur from internal method// instance calls
            print('Improper Call Structure')
            print(f'Call Details : {parameters}')
            pass


