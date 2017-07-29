import pandas as pd
import datetime
import numpy as np
import utils

def rsi_calc(data):
	# Window length for moving average
	window_length = 14

	close = data['close']
	# Get the difference in price from previous step
	delta = close.diff()
	# Get rid of the first row, which is NaN since it did not have a previous 
	# row to calculate the differences
	delta = delta[1:] 

	# Make the positive gains (up) and negative gains (down) Series
	up, down = delta.copy(), delta.copy()
	up[up < 0] = 0
	down[down > 0] = 0

	# Calculate the EWMA
	roll_up1 = pandas.stats.moments.ewma(up, window_length)
	roll_down1 = pandas.stats.moments.ewma(down.abs(), window_length)

	# Calculate the RSI based on EWMA
	RS1 = roll_up1 / roll_down1
	RSI1 = 100.0 - (100.0 / (1.0 + RS1))
   # print dir(data.rolling())
	# Calculate the SMA
	roll_up2 = data.rolling(up, window_length)
	roll_down2 = data.rolling(down.abs(), window_length)

	# Calculate the RSI based on SMA
	RS2 = roll_up2 / roll_down2
	RSI2 = 100.0 - (100.0 / (1.0 + RS2))

	# Compare graphically
	plt.figure()
	RSI1.plot()
	RSI2.plot()
	plt.legend(['RSI via EWMA', 'RSI via SMA'])
	plt.show()

def RSI(series, period):
	delta = series.diff().dropna()
	u = delta * 0
	d = u.copy()
	u[delta > 0] = delta[delta > 0]
	d[delta < 0] = -delta[delta < 0]
	u[u.index[period-1]] = np.mean( u[:period] ) #first value is sum of avg gains
	u = u.drop(u.index[:(period-1)])
	d[d.index[period-1]] = np.mean( d[:period] ) #first value is sum of avg losses
	d = d.drop(d.index[:(period-1)])
	rs = pd.stats.moments.ewma(u, com=period-1, adjust=False) / \
	pd.stats.moments.ewma(d, com=period-1, adjust=False)
	rsi_values = 100 - 100 / (1 + rs)
	print(len(rsi_values))
	# plt.figure()
	# rsi_values.plot()
	# plt.legend(['RSI (14, close)'])
	# plt.show()
	return rsi_values