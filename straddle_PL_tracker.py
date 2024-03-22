import time
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from tdamr_api import TDclient as tdc
from dbm_spl import db_operator

def strd_pl():


    stock = 'SPY'
    date = '2024-01-19'
    strike_list = [ '479.0/478.0', '480.0/477.0', '478.0/479.0'] #call_strike / put_strike

    td_api = tdc()

    data_raw = td_api.option_chain(details=[stock, False])
    data = td_api.sort_data_into_data_frames(data_raw)

    puts_chain = data[1] # 0 would be calls
    calls_chain = data[0]

    single_put_chain = puts_chain[date]
    single_call_chain = calls_chain[date]



    single_put_chain = single_put_chain[['bid', 'ask', 'intrinsicValue']]
    single_call_chain = single_call_chain[['bid', 'ask', 'intrinsicValue']]

    #print(single_call_chain)

    #single_chain['spread'] = single_chain['ask'] - single_chain['bid']

    strad_values = {}

    #strikes_list = list(single_call_chain.index)

    for strike in strike_list:

        call_strike = strike.split('/')[0]
        put_strike =  strike.split('/')[1]

        value = round(float(single_put_chain.loc[put_strike]['ask'] + single_call_chain.loc[call_strike]['ask']), 2)
        strad_values[strike] = value


    return(strad_values)

    #single_call_chain.loc['477.0']['bid'])

db = db_operator('spl')

'''while True:

    #db.create_table_spl('SPY240119', [ '479.0/478.0', '480.0/477.0', '478.0/479.0'])
    a_data = strd_pl()
    print(a_data)
    db.add_strdPL_data(a_data, 'SPY240119')
    time.sleep(5)

'''

pull_data = db.pull_data(table_name='SPY240119')

df = pd.DataFrame(pull_data, columns =['Index', '479.0/478.0', '480.0/477.0', '478.0/479.0'])

p_data = list(map(float, df['480.0/477.0']))



ll = len(p_data)
diff = []

for i in enumerate(p_data):
    value = i[1]

    end_index = i[0] + (12*5)
    if end_index  > ll-1:
        break

    else:
        end_value = p_data[end_index]
        diff.append(end_value-value)


diff = [round(value, 3)  for value in diff]
#print(diff)

plt.hist(diff)
plt.show()





