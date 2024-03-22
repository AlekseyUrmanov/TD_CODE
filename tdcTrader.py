from XlsxTesting import TDclient
import time
import threading
import datetime
import matplotlib.pyplot as plt




tdc = TDclient()


# today_dat= str(datetime,datetime,now().date())



x = tdc.option_chain(details = ['SPY', False])

xx = tdc.sort_data_into_data_frames(x)
xx = xx[0]['2023-03-02']

print(xx)


c = tdc.get_quote(details=['SPY', True])

print(c)
#print(xx)











# Date validation
# Buy 100 Shares, sell ATM call
# AT close --> keep full premium or sell 100 shares + full premium.
# AT open, no shares --> Can buy ? yes --> buy, sell ATM call, no --> sell put at entry value
# repeat
'''
x = [31, 31.5, 32, 32.5, 33, 33.5, 34, 34.5, 35, 35.5, 36, 36.5, 37, 37.5] # strikes
y = [3,5,8,13, 21, 34, 54, 81, 115, 153, 198, 243, 294, 340 ] # price

plt.plot(x,y)
plt.show()


'''