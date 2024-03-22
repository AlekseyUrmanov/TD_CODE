import pandas as pd
import requests
import json


def snc(date):
    url = 'https://api.nasdaq.com/api/calendar/dividends?date={}'.format(date)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
        # Add more headers if required
    }
    response = (requests.get(url, headers=headers)).json()
    data = response["data"]['calendar']['rows']
    return data


def sort_data(data):
    sorted_data = {}
    for entry in data:
        symbol = str(entry['symbol'])
        cash_div_payment = str(entry['dividend_Rate'])
        annual_cash_div_payment = str(entry['indicated_Annual_Dividend'])
        pay_date = str(entry['payment_Date'])
        ex_date = str(entry['dividend_Ex_Date'])

        sorted_data[symbol] = {'cash': cash_div_payment, 'yearly_cash': annual_cash_div_payment, 'pay_date': pay_date,
                               'ex_date': ex_date}

    return sorted_data


