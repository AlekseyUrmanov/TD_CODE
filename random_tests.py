import time

import matplotlib.pyplot as plt
import pickle
import pandas
import pandas as pd
import json
from XlsxTesting import TDclient
import numpy as np


class short_straddle_tracker:

    def __init__(self, tickers, update_interval):
        self.tickers = tickers
        self.all_data = {}
        self.tdc = TDclient()
        self.update_interval = update_interval

    # function to initiize data

    # function to update all data for every ticker

    # track how many times each straddle becomes profitable
    # or if the straddles even become profitable
    # find ratio of profitable strads, trade strads

    def run(self):
        self._set_up()
        while True:
            self._update()
            print(self.all_data['AMC']['2023-03-31'])
            time.sleep(self.update_interval)

    def _set_up(self):
        for ticker in self.tickers:

            raw_json = self.tdc.option_chain(details=[f'{ticker}', False])

            data = self.tdc.sort_data_into_data_frames(raw_json)

            call_dfs = data[0]
            put_dfs = data[1]

            all_straddle_frames = {}

            for i in range(len(list(call_dfs.keys()))):
                date = list(call_dfs.keys())[i]

                call_df = call_dfs[date][['bid', 'ask']]
                put_df = put_dfs[date][['bid', 'ask']]
                call_df = call_df.rename(columns={"bid": "cbid", "ask": "cask"})

                straddle_frame = pd.concat([call_df, put_df], axis=1)
                straddle_frame['short_strad'] = straddle_frame['cbid'] + straddle_frame['bid']
                straddle_frame['prof'] = 0

                all_straddle_frames[date] = straddle_frame

            self.all_data[ticker] = all_straddle_frames
        time.sleep(5)

    def _update(self):

        for ticker in self.tickers:
            raw_json = self.tdc.option_chain(details=[f'{ticker}', False])

            data = self.tdc.sort_data_into_data_frames(raw_json)

            call_dfs = data[0]
            put_dfs = data[1]

            for i in range(len(list(call_dfs.keys()))):
                date = list(call_dfs.keys())[i]

                call_df = call_dfs[date][['bid', 'ask']]
                put_df = put_dfs[date][['bid', 'ask']]
                call_df = call_df.rename(columns={"bid": "cbid", "ask": "cask"})

                combine_df = pd.concat([call_df, put_df], axis=1)
                cost_to_close = combine_df['cask'] + combine_df['ask']

                straddle_frame_by_date = self.all_data[ticker][date]
                straddle_frame_by_date['pl'] = straddle_frame_by_date['short_strad'] - cost_to_close

                straddle_frame_by_date['cbid'] = call_df['cbid']
                straddle_frame_by_date['cask'] = call_df['cask']
                straddle_frame_by_date['bid'] = put_df['bid']
                straddle_frame_by_date['ask'] = put_df['ask']

                updated_df = straddle_frame_by_date

                self.all_data[ticker][date] = updated_df
        self._analyze()

    def _analyze(self):
        for ticker in self.tickers:

            data = self.all_data[ticker]

            for date in data:
                self.all_data[ticker][date]['prof'] = self.all_data[ticker][date].apply(lambda x:
                                                          1 if x['prof'] == 1 or x['pl'] > 0
                                                          else 0, axis=1)


obj = short_straddle_tracker(['AMC'], 30)

obj.run()















