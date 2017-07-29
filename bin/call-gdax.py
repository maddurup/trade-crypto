import gdax
import pprint, time
import pandas as pd
import rsi, strategies
import matplotlib.pyplot as plt
import csv
from datetime import datetime

start_time = datetime.now()

def plot_rsi(x,y):
	plt.figure()
	plt.plot(x, y, lw = 1)
	plt.legend(['RSI (14, close)'])
	plt.show()


def red_green(open_price, close_price):
	if int(open_price) > int(close_price):
		return 'green'
	else:
		return 'red'

def transform_data(df):
	# this function is to add additiona variables for the analysis and stratagies.

	# defining reg green candles
	df['red_green'] = ''
	df['red_green'][df['open'] > df['close']] = 'red'
	df['red_green'][df['open'] <= df['close']] = 'green'

	# getting previous reg green indicators
	df['red_green_prev_1'] = df['red_green'].shift()
	df['red_green_prev_2'] = df['red_green'].shift(2)
	df['red_green_prev_3'] = df['red_green'].shift(3)

	# define previous close
	df['prev_close_1'] = df['close'].shift()
	df['prev_close_2'] = df['close'].shift(2)
	df['prev_close_3'] = df['close'].shift(3)

	# Time Stuff
	df['time'] = pd.to_datetime(df["time"], unit='s')
	df['date'] = df["time"].dt.date
	df['time_time'] = df["time"].dt.time

	# RSI
	df['rsi'] = rsi.RSI(df['close'], 14)

	return df

def main():
	# initializers
	output_end_file = 'C:\Python36-32\other_packages\datafiles\crypto-trade.csv'
	coin_to_trade = 'LTC-USD'
	chart_grain = 60
	# initializing connection to GDAX
	public_client = gdax.PublicClient()
	recent_historic_values = public_client.get_product_historic_rates(coin_to_trade, granularity=chart_grain)
	# pprint.pprint(recent_historic_values)
	recent_historic_values = list(reversed(recent_historic_values))

	# converting Json to DataFrame
	df = pd.DataFrame(recent_historic_values)
	df.columns = [ 'time', 'low', 'high', 'open', 'close', 'volume' ]
	df.is_copy = False
	df = transform_data(df)

	print(df.tail(50))


	df = strategies.three_green_strat(df)


	df.to_csv(output_end_file, sep=',')        
	#plot_rsi(df['time_time'][-60:], df['rsi'][-60:])


	#rsi.rsi_calc(df)
	#print(rsi.RSI(df['close'], 14))

	end_time = datetime.now()
	print("time ran : - " + str(end_time - start_time))

if __name__ == "__main__":
    main()





