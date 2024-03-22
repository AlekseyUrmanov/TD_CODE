import tdamr_api as tdp
import sqlite3
import json
import time


tdc = tdp.TDclient()


data = tdc.get_quotes(details=[['F', 'GOOG', 'CMG', 'NVDA', 'HD', 'SPY'], False])


#Options_data = tdc.option_chain(details=['F', False])
#Options_data = tdc.sort_data_into_data_frames(Options_data)



# check spread, bid, ask
# track avg spread

# condition to remove order
# if ask is closer to our position than 50% of spread


# place bid order
# if not filled by the next loop cycle
# move it up.
# repeat

# place order at ask.
# if not filled by the next loop cycle
# move it down.
# repeat



# monitor spread process is started







class position:
    def __init__(self, shares, ticker):
        self.shares = shares
        self.ticker = ticker


print(data)



