import json

import requests
import pandas as pd


class TDclient:

    def __init__(self):

        self.ck = "Y1KS0BMRKRBSI6CVNYIHHN1NVF3VUI2J"
        self.at = 'Bearer dXmHRnlbQYmy0akCPqaqYEgUFPsWwos+wQCXQa30FMU8zFYyNb82vnNWUx9JBh78QIEGbbFiETPPsYPzGm9pj+LQvPx9G5A2+wJWkn8vVBnJXdc1a43CyViv2ze2TZ1qx5Zrk0IP9ElP3QBTbOE1uDBETrPmUN8e7f25a4id4eDtoeXYQrufTD1G3EaS86RulcLrDWvDtN4FNo9vR748E3C6eHoQW+k6c82wwo12+hg21MufF0bpIp4cRE1Df2Lgd/mYC1iW7RCzbHoADD6u2T+PBkC0SQBp6WCsHYqiGEnq1ZoAXhD7BquZ7s4fOIOCM1e1esJU7edEFZ4x2eQt16Us/Ug3Vo/sWuq/m6D1Y5lq7mmsQgcq9FaiciY1CwU6iHWZDEeyhM9A6ljPVv4BVyI0L7xxWeYjox7jkIZ6xICy3e+nQI0m5BT8rrqtZJbVwtN4eVbPoRX728uizVUHEEzXZG2QKoHV0Fu6LoBdGbScpQjhvZeGs4iDtPiCMwpQG/TJjVo9ewYNdU2hYukmYSAFfGKo6dcwHTh8HSqfiwjMU1KXb100MQuG4LYrgoVi/JHHvlTyhKP3MeHZdiXryRRoydSq6xKx1hj6WpPt4BEuHVis8/e9Y4OFIiCJXgKZsrhj2rbO9rEl0pOefM/rrAwG9MBwtJOBy9P8uG3Zhih0Wf4iaExwKaMC7q3BufHmf+5HcRNvP0aYHbZ33jwqr17H1pZ/52lsXb/i5Tn4vK0hG6wX2jDiTbx7hKr5LICxYrCOeSdEIVjkK+oihJwsFrXU/YYJmIUWw1hAhMnO9YdMjxIzegwZOSDA/vQNEukOzRlsvzo71RH5nH0KVVjiRJ5fNT5To5XuJ+QFvgaWs3rf1+uEYAZ5E9K9M5z8bGf+r1RVkoxNb0ZRQ3D8FsIb4b/TjmaiVZzKc5tFjzfFg1PfHtw9iKLR+MkMQkwXtfBdutsUg2tTtjltCUFjui/f/RYBpxvgPU7DPmoZI7/yUBEw4S3trcoZCzRY3k2IWm0npIcDAo9lLkA6c27jlxMnavtcLm3EyJ6WYexVESYMEkmnp9E2lv2G9kkFNkbih+7W2Og6oGpEEOMJr9gLLAsHlxuuhvRt5Bm955r2RFfmsnUPeYFrLlyD2g==212FD3x19z9sWBHDJACbC00B75E'
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
        url = 'https://api.tdameritrade.com/v1/accounts/236642469/orders'
        # format tickr inserts the stock ticker variable, r is raw string.
        headers = {
            'Authorization': self.at
        }

        params = {
            'status': 'WORKING', # WORKING, PENDING_ACTIVATION (after hours), CANCELLED.
            #'fields': details
        }

        response = requests.get(url, params=params, headers=headers)
        content = self.response_processing(response, self.get_account_data, details)
        return content

    def get_quote(self, details=[]):

        symbol = details[0]
        real_time = details[1]

        # with authentication there will be real_time_data entitled : true
        url = 'https://api.tdameritrade.com/v1/marketdata/{}/quotes'.format(symbol)

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



    def get_quotes(self, details=[]):

        symbols = details[0]
        real_time = details[1]

        # with authentication there will be real_time_data entitled : true
        url = 'https://api.tdameritrade.com/v1/marketdata/quotes'

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
                'symbol':symbols

            }
            header = {}

        response = requests.get(url=url, params=params, headers=header)
        content = self.response_processing(response, self.get_quote, symbols)
        return content


    def get_limit_order_book(self, ticker):
        endpoint = format("https://api.tdameritrade.com/v1/marketdata/{}/orderbook", ticker)

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
                'strikeCount': '14',
                'includeQuotes': 'FALSE',
                'strategy': 'SINGLE',
                'range': 'ITM'
            }

            header = {}

        response = requests.get('https://api.tdameritrade.com/v1/marketdata/chains', params=params, headers=header)
        content = self.response_processing(response, self.option_chain, details)
        return content


    def specific_option_chain_quote(self, symbol, real_time = False):

        ticker = symbol.split('_')[0]
        date_string = symbol.split('_')[1]

        day = date_string[2:4]
        mon = date_string[0:2]
        year = date_string[4:6]

        full_date = '20'+year + '-' + mon + '-' + day

        if "P" in symbol:
            strike = symbol.split('P')[1]
            contract_type = 'PUT'
            pc_query = 'putExpDateMap'
        else:
            strike = symbol.split('C')[1]
            contract_type = 'CALL'
            pc_query = 'callExpDateMap'

        if real_time:

            params = {
                'apikey': self.ck,
                'symbol': ticker,
                'contractType': contract_type,
                'includeQuotes': 'TRUE',
                'strike': strike,
                'toDate': full_date,
            }

            header = {
                'Authorization': self.at,
                'Content-Type': 'application/json'
            }

            response = requests.get('https://api.tdameritrade.com/v1/marketdata/chains', params=params, headers=header)
            content = self.response_processing(response, self.option_chain, symbol)


            contract_data = content[pc_query]
            contract_data = contract_data[list(contract_data.keys())[0]]
            contract_data = contract_data[list(contract_data.keys())[0]]
            contract_data = contract_data[0]

            underlying = content['underlying']

            return {'asset':underlying, 'option':contract_data}

        else:
            pass


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



    def cancel_option_order(self, OID):
        
        url = 'https://api.tdameritrade.com/v1/accounts/236642469/orders/{}'.format(OID)

        headers = {
            'Authorization': self.at,
            #'Content-Type': 'application/json',
        }

        '''parameters = {



            'orderId': OID
        }'''

        response = requests.delete(url=url, headers=headers)
        print(response)

        content = self.response_processing(response, self.cancel_option_order, parameters=OID)

        return(content)



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
        print(full_code)
        self.at = full_code


    def response_processing(self, response, func_call, parameters):
        #show sresponses that came, update tokens and variables, recall operations, keep operation log
        print(func_call.__name__.upper())
        response_code = response.status_code
        print(response_code)

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
                print(parameters)
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
            print(parameters)
            pass


