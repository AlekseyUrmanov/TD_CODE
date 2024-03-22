# Imports

import requests
import pandas as pd
import time
import json
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import confusion_matrix

# Abstract

"""In this project, I'll be using TD Ameritrade API to get the daily Open High Low Close (OHLC) candle data for all
SP 500 companies. Though there are millions of thing you can do, I decided to try to apply the principles of binary
classification to make some predictions. My Binary variable will be indicated by 1: where the high price of the day is
greater than the close price of the previous day; 0 otherwise. I will try to determine if a model can use the
percentage change in volume over the trading days and % change in daily price, to determine if the next days high price
will be greater than the previous days close price.
"""

# Source

"""I obtained my data from TD Ameritrade using my developer API keys. Access to these keys is no longer available. Thus,
I downloaded all the data and stored it locally, I attached the data file so the code can be ran.
URL : "https://api.tdameritrade.com/v1/marketdata/{}/pricehistory", {} places ticker inside

500 companies multiplied by roughly 250 days of data makes around 125,000 rows of OHLCV
less any companies which returned bad requests, so around 120,000 rows

I could have gone with many more if I increased the granularity of the data from days to hours and so on

"""

# Data Gathering / # Data Cleaning


"""
Data is stored locally in json files, in {symbol}_1YD.json format. 
I wrote a function to retrieve all of it and place it into pandas data frames. 
A function allows me to create a separate dataframe for each ticker, if I so wish to reuse it in the future
without all 500 companies. 


I did not not to clean the data as much as I needed to add more columns to it, I added a daily_profit loss column 
which is simply the difference between the close and open price. I did not end up using it in my initial analysis, 
but I might use it later on in adjusting the model or doing some k-means or linear regression. I also got the gain/loss 
per day as a percentage to make it comparable across all 120,000 rows. I did the same for the volume, I calcluated the 
changes and made a delta_volume column. I then shifted the both of these % columns down 1 row. 

The target binary variable that I will be predicting I also needed to add; is the condition that the high price of
the day is greater than the close price of the previous day. I also added a ticker column so  that I could 
hierarchy index the combined data frame. 

As I mentioned earlier I shifted the two columns down because I needed to be using historical values to predict 
future values. 

"""

# all 500 companies
sp_500 = ['MMM', 'AOS', 'ABT', 'ABBV', 'ABMD', 'ACN', 'ATVI', 'ADM', 'ADBE', 'ADP', 'AAP', 'AES', 'AFL', 'A', 'AIG',
          'APD', 'AKAM', 'ALK', 'ALB', 'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AMCR',
          'AMD', 'AEE', 'AAL', 'AEP', 'AXP', 'AMT', 'AWK', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS', 'ANTM',
          'AON', 'APA', 'AAPL', 'AMAT', 'APTV', 'ANET', 'AIZ', 'T', 'ATO', 'ADSK', 'AZO', 'AVB', 'AVY', 'BKR', 'BALL',
          'BAC', 'BBWI', 'BAX', 'BDX', 'WRB', 'BRK.B', 'BBY', 'BIO', 'TECH', 'BIIB', 'BLK', 'BK', 'BA', 'BKNG', 'BWA',
          'BXP', 'BSX', 'BMY', 'AVGO', 'BR', 'BRO', 'BF.B', 'CHRW', 'CDNS', 'CZR', 'CPT', 'CPB', 'COF', 'CAH', 'KMX',
          'CCL', 'CARR', 'CTLT', 'CAT', 'CBOE', 'CBRE', 'CDW', 'CE', 'CNC', 'CNP', 'CDAY', 'CERN', 'CF', 'CRL', 'SCHW',
          'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CTXS', 'CLX', 'CME', 'CMS',
          'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'COP', 'ED', 'STZ', 'CEG', 'COO', 'CPRT', 'GLW', 'CTVA', 'COST',
          'CTRA', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DAL', 'XRAY', 'DVN', 'DXCM', 'FANG',
          'DLR', 'DFS', 'DISH', 'DIS', 'DG', 'DLTR', 'D', 'DPZ', 'DOV', 'DOW', 'DTE', 'DUK', 'DRE', 'DD', 'DXC', 'EMN',
          'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMR', 'ENPH', 'ETR', 'EOG', 'EPAM', 'EFX', 'EQIX', 'EQR', 'ESS',
          'EL', 'ETSY', 'RE', 'EVRG', 'ES', 'EXC', 'EXPE', 'EXPD', 'EXR', 'XOM', 'FFIV', 'FDS', 'FAST', 'FRT', 'FDX',
          'FITB', 'FRC', 'FE', 'FIS', 'FISV', 'FLT', 'FMC', 'F', 'FTNT', 'FTV', 'FBHS', 'FOXA', 'FOX', 'BEN', 'FCX',
          'AJG', 'GRMN', 'IT', 'GE', 'GNRC', 'GD', 'GIS', 'GPC', 'NWSA', 'NWS', 'NEE', 'NLSN', 'NKE', 'NI', 'NDSN',
          'NSC', 'NTRS', 'NOC', 'NLOK', 'NCLH', 'NRG', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ORLY', 'OXY', 'ODFL', 'OMC',
          'OKE', 'ORCL', 'OGN', 'OTIS', 'PCAR', 'PKG', 'PARA', 'PH', 'PAYX', 'PAYC', 'PYPL', 'PENN', 'PNR', 'PEP',
          'PKI', 'PFE', 'PM', 'PSX', 'PNW', 'PXD', 'PNC', 'POOL', 'PPG', 'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU',
          'PEG', 'PTC', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RL', 'RJF', 'RTX', 'O', 'REG', 'REGN',
          'RF', 'RSG', 'RMD', 'RHI', 'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'SPGI', 'CRM', 'SBAC', 'SLB', 'STX', 'SEE',
          'SRE', 'NOW', 'SHW', 'SBNY', 'SPG', 'SWKS', 'SJM', 'SNA', 'SEDG', 'SO', 'LUV', 'SWK', 'SBUX', 'STT', 'STE',
          'SYK', 'SIVB', 'SYF', 'SNPS', 'SYY', 'TMUS', 'TROW', 'TTWO', 'TPR', 'TGT', 'TEL', 'TDY', 'TFX', 'TER',
          'TSLA', 'TXN', 'TXT', 'TMO', 'TJX', 'TSCO', 'TT', 'TDG', 'TRV', 'TRMB', 'TFC', 'TWTR', 'TYL', 'TSN', 'USB',
          'UDR', 'ULTA', 'UAA', 'UA', 'UNP', 'UAL', 'UNH', 'UPS', 'URI', 'UHS', 'VLO', 'VTR', 'VRSN', 'VRSK', 'VZ',
          'VRTX', 'VFC', 'VTRS', 'V', 'VNO', 'VMC', 'WAB', 'WMT', 'WBA', 'WBD', 'WM', 'WAT', 'WEC', 'WFC', 'WELL',
          'WST', 'WDC', 'WRK', 'WY', 'WHR', 'WMB', 'WTW', 'WYNN', 'XEL', 'XYL', 'YUM', 'ZBRA', 'ZBH', 'ZION', 'ZTS',
          'GILD', 'GL', 'GPN', 'GM', 'GS', 'GWW', 'HAL', 'HIG', 'HAS', 'HCA', 'PEAK', 'HSIC', 'HSY', 'HES', 'HPE',
          'HLT', 'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HWM', 'HPQ', 'HUM', 'HII', 'HBAN', 'IEX', 'IDXX', 'ITW', 'ILMN',
          'INCY', 'IR', 'INTC', 'ICE', 'IBM', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG', 'IVZ', 'IPGP', 'IQV', 'IRM', 'JBHT',
          'JKHY', 'J', 'JNJ', 'JCI', 'JPM', 'JNPR', 'K', 'KEY', 'KEYS', 'KMB', 'KIM', 'KMI', 'KLAC', 'KHC', 'KR',
          'LHX', 'LH', 'LRCX', 'LW', 'LVS', 'LDOS', 'LEN', 'LLY', 'LNC', 'LIN', 'LYV', 'LKQ', 'LMT', 'L', 'LOW',
          'LUMN', 'LYB', 'MTB', 'MRO', 'MPC', 'MKTX', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MTCH', 'MKC', 'MCD', 'MCK',
          'MDT', 'MRK', 'FB', 'MET', 'MTD', 'MGM', 'MCHP', 'MU', 'MSFT', 'MAA', 'MRNA', 'MHK', 'MOH', 'TAP', 'MDLZ',
          'MPWR', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MSCI', 'NDAQ', 'NTAP', 'NFLX', 'NWL', 'NEM']


def run_ohlc_json(symbol):

    try:
        # Data Gathering
        #/Users/nadia/Desktop/PycharmProjects/TDFinanceDataTesting/ohlc_historical_500_json_data
        raw_data = open(f'ohlc_historical_500_json_data/{symbol}_1YD.json')
        data = json.load(raw_data)
        df = pd.DataFrame(data)

        # Data Cleaning / Modification
        df['ticker'] = symbol
        df['daily_pl'] = df['close'] - df['open']
        df['daily_pl_%'] = round((((df['close'] / df['open']) - 1)*100), 2)
        #df['dpl_whole'] = (100 / df['daily_pl_%']) * df['daily_pl']
        df['delta_volume'] = (df['volume'].pct_change())*100
        df['high_more_prev_close'] = 0

        # we also add a VWAP colummn (volume weighted average price)

        df['typical_price'] = (df['high'] + df['low'] + df['close']) / 3
        df['value_traded'] = df['typical_price'] * df['volume']

        df['cumulative_value'] = df['value_traded'].cumsum()
        df['cumulative_volume'] = df['volume'].cumsum()
        df['vwap'] = df['cumulative_value'] / df['cumulative_volume']

        df.loc[df['high'] > df['close'].shift(), 'high_more_prev_close'] = 1

        df['vwap_shift'] = df['vwap'].shift(1)
        df['vol_%_shift_down'] = df['delta_volume'].shift(1)  # shift down to predict using historical values
        df['daily_pl_%_shift_down'] = df['daily_pl_%'].shift(1)

        df = df.dropna()

        return df

    except Exception as error:
        pass


all_frames = []

for ticker in sp_500:
    df = run_ohlc_json(ticker)
    all_frames.append(df)

full_df = pd.concat(all_frames)
# 124,634 OHLCV data

full_df_indexed = (full_df.set_index(['ticker']))
# indexed by ticker






# Understanding Data

print(full_df_indexed['high_more_prev_close'].value_counts())


print(full_df_indexed.info())
print(full_df_indexed.describe())
print(full_df_indexed.sample(10))

"""
For the purpose of our first analysis, we can take a look at what the % changes in volumes and daily P/L look like

"""

plt.subplot(1,2,1)
y = list(full_df_indexed['vol_%_shift_down'])
x = list(range(len(y)))
plt.scatter(x, y)
plt.title('% Volume Changes Distribution')
plt.subplot(1,2,2)
y = list(full_df_indexed['daily_pl_%_shift_down'])
x = list(range(len(y)))
plt.scatter(x, y)
plt.title('% Price Changes Distribution')

plt.show()

# Data Modeling


"""
Is it possible to determine if the high price of a trading day will reach beyond the close price of the previous day
"""


# Modeling Configuration

"""
Model will predict the binary high_more_prev_close column.
The % change in price and % change in volume of the previous trading (close price) day will be the features
"""

# Apply the model


X = full_df_indexed[['vol_%_shift_down', 'daily_pl_%_shift_down']] # predictor
y = full_df_indexed['high_more_prev_close'] # target data


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
# 75% data train size

ss_train = StandardScaler()
X_train = ss_train.fit_transform(X_train)

ss_test = StandardScaler()
X_test = ss_test.fit_transform(X_test)


model = LogisticRegression(random_state=0)
model.fit(X_train, y_train)


# Evaluate the model


predictions = model.predict(X_test)

cm = confusion_matrix(y_test, predictions)

TN, FP, FN, TP = confusion_matrix(y_test, predictions).ravel()

print('True Positive(TP)  = ', TP)
print('False Positive(FP) = ', FP)
print('True Negative(TN)  = ', TN)
print('False Negative(FN) = ', FN)

acc = (TP + TN) / (TP + FP + TN + FN)

print(f'BC accuracy {acc}\n')

# if we try changing the test to train data ratio from 0.25 --> 0.50

X = full_df_indexed[['vol_%_shift_down', 'daily_pl_%_shift_down']] # predictor
y = full_df_indexed['high_more_prev_close'] # target data


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50, random_state=0)


ss_train = StandardScaler()
X_train = ss_train.fit_transform(X_train)

ss_test = StandardScaler()
X_test = ss_test.fit_transform(X_test)


model = LogisticRegression(random_state=0)
model = model.fit(X_train, y_train)


# Evaluate the model


predictions = model.predict(X_test)
print(list(predictions))

cm = confusion_matrix(y_test, predictions)

TN, FP, FN, TP = confusion_matrix(y_test, predictions).ravel()

print('True Positive(TP)  = ', TP)
print('False Positive(FP) = ', FP)
print('True Negative(TN)  = ', TN)
print('False Negative(FN) = ', FN)

acc = (TP + TN) / (TP + FP + TN + FN)

print(f'BC accuracy {acc}')




# Summary


"""
The thing with time series data, is that the underlying theory is random walk. The system that is the market is 
supposedly random, therefore, there are no underlying patterns. But that's not necessarily true. There's no reason
to go into details. But this data analysis was just another attempt at quantifying random movement. It's like mining for 
gold; you choose a random start and start shuffling your pan, I took a few random % change variables and shuffled. 

My result's were inconclusive. Yes, the model has 80% accuracy. But this is simply too good to be true. Therefore, 
I conclude that I made an error somewhere. I'm not a stats PHD to discern where I went wrong, Probably back testing 
fallacy, over fitting, and what not. This would be a lot more interesting If I had millions/billions of data points. 
Then the results would be significant. 


The issue I'm having is that the model is not outputting True Negatives or False Negatives. Additionally, 
when I change the predictors, the model accuracy barely changes. 

I'm also not exactly sure how to practically apply this model. 

"""




