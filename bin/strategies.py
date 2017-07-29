def three_green_strat(data):
	orders = 0
	data['buy_sell'] = 'WAIT'
	data['buy_sell'][(data['red_green_prev_3'] == 'red') & (data['red_green_prev_2'] == 'green') & (data['red_green_prev_1'] == 'green') & (data['red_green'] == 'green')] = 'BUY'
	data['buy_sell'][(data['red_green_prev_1'] == 'red') & (data['red_green'] == 'red')] = 'SELL'
	return data