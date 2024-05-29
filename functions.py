from datetime import datetime , timedelta
from zerodha_api import kite_client as kite


def output(aa):
	output = aa -2
	return output



def Multiplier(aa, bb):
	output = aa * bb 
	return output


def calculate_profit(buy_price, sell_price, shares):

    profit = (sell_price - buy_price) * shares
    return profit


def LTP(name):

	zrd_name = 'NSE:'+ name
	data = kite.quote([zrd_name])
	ltp = data[zrd_name]['last_price']
	return ltp

def OPENN(name):
	openn = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['open']
	return openn

def HIGH(name):
	high = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['high']
	return high

def LOW(name):
	low = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['low']
	return low

def CLOSE(name):
	close = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['close']
	return close

def BID(name):
	bid_price = kite.quote(['NSE:'+ name])['NSE:'+ name]['depth']['buy'][0]['price']
	return bid_price

def ASK(name):
	Ask_price = kite.quote(['NSE:'+ name])['NSE:'+ name]['depth']['sell'][0]['price']
	return Ask_price

def VOLUME(name):
	volume = kite.quote(['NSE:'+ name])['NSE:'+ name]['volume']
	return volume

def l_ohlc_v(name):
	zrd_name = 'NSE:'+ name
	data = kite.quote([zrd_name])
	ltp = data[zrd_name]['last_price']
	openn = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['open']
	high = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['high']
	low = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['low']
	close = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['close']
	volume = kite.quote(['NSE:'+ name])['NSE:'+ name]['volume']
	return ltp,openn,high,low,close,volume

def ob():
	margins = kite.margins()
	ob = margins['equity']['available']['opening_balance']
	return ob

def ohlc(name):
	
	openn = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['open']
	high = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['high']
	low = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['low']
	close = kite.ohlc(['NSE:' + name])['NSE:' + name]['ohlc']['close']
	
	return openn,high,low,close,

def BID_1(name):
	data = kite.quote('NSE:' + name)
	bid_price = data['NSE:'+name]['depth']['buy'][0]['price']
	return bid_price

def lb():
	margins = kite.margins()
	lb = margins['equity']['available']['live_balance']
	return lb

def pnl(name):
	sym = name
	pos = kite.positions()
	net_pos = pos['net']
	len_net_pos = len(net_pos)

	for x in range(len_net_pos):
		if net_pos[x]['tradingsymbol']==sym:
			pnl = (round(pos['net'][x]['pnl'],2))
			return pnl

def net_pnl():
	traded_stocks_pnl = []
	pos = kite.positions()
	net_pos = pos['net']
	len_net_pos = len(net_pos)

	for x in range(len_net_pos):
		a = round(net_pos[x]['pnl'],2)
		traded_stocks_pnl.append(a)
	value = (sum(traded_stocks_pnl))
	return value

def day_pnl():
	traded_stocks_pnl = []
	pos = kite.positions()
	net_pos = pos['day']
	len_net_pos = len(net_pos)

	for x in range(len_net_pos):
		a = round(net_pos[x]['pnl'],2)
		traded_stocks_pnl.append(a)
	value = (sum(traded_stocks_pnl))
	return value

def LTP_NFO(name):

	zrd_name = 'NFO:'+ name
	data = kite.quote([zrd_name])
	ltp = data[zrd_name]['last_price']
	return ltp

def BID_NFO(name):
	bid_price = kite.quote(['NFO:'+ name])['NFO:'+ name]['depth']['buy'][0]['price']
	return bid_price
