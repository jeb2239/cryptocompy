# get.py
import json
import requests


def get_coin_information(coins='all'):
	"""
	Get general information about all the coins available on 
	cryptocompare.com.
	
	Args:
		coins: Default of 'all' returns complete list. Otherwise a list of coin
			symbols can be used.

	Returns:
		The function returns a dictionairy containing individual dictionairies 
		for the coins specified by the input. The key of the top dictionary 
		corresponds to the coin symbol. Each coin dictionary has the following 
		structure:
			{'Algorithm' : ...,
			 'CoinName': ...,
			 'FullName': ...,
			 'FullyPremined': ...,
			 'Id': ...,
			 'ImageUrl': ...,
			 'Name': ...,
			 'PreMinedValue': ...,
			 'ProofType': ...,
			 'SortOrder': ...,
			 'TotalCoinsFreeFloat': ...,
			 'TotalCoinSupply': ...,
			 'Url': ...}
	"""
	
	# http request
	url = "https://www.cryptocompare.com/api/data/coinlist/"
	r = requests.get(url)

	# data extraction
	data = r.json()
	message = data["Message"]
	coin_data = data["Data"]

	print(message)

	# coins specified
	if coins != 'all':
		coin_data = {c: coin_data[c] for c in coins}

	return coin_data


def get_latest_price(fsyms, tsyms, e='all', full=False, format='raw'):
	"""
	Get latest full or compact price information in display or raw format for 
	the specified FROM-TO currency pairs.

	Args:
		fsyms: List containing the FROM symbols.
		tsyms: List containing the TO symbols.
		e: Default returns average price across all markets. Can be set to the
			name of a single market.
		full: Default of False returns only the latest price. True returns the 
			following dictionary structure:
				{'TYPE': ..., 
			 	 'LASTVOLUME': ..., 
			 	 'CHANGE24HOUR': ..., 
			 	 'LASTUPDATE': ...,, 
			 	 'OPEN24HOUR': ..., 
			 	 'MKTCAP': ...,
			 	 'FLAGS': ...,
			 	 'LASTVOLUMETO': ...,
			 	 'VOLUME24HOURTO': ...,
			 	 'LASTTRADEID': ...,
			 	 'FROMSYMBOL': ...,
			 	 'SUPPLY': ...,
			 	 'CHANGEPCT24HOUR': ...,
			 	 'TOSYMBOL': ...,
			 	 'LOW24HOUR': ...,
			 	 'VOLUME24HOUR': ...,
			 	 'HIGH24HOUR': ...,
			 	 'LASTMARKET': ...,
			 	 'PRICE': ...,
			 	 'MARKET' ...}
		format: Default returns the 'RAW' format. Can be set to 'DISPLAY' 
			format.
	Returns:
		Returns a dictionary containing the latest price pairs...



	"""

	# full set to True
	if not full:
		base_url = "https://min-api.cryptocompare.com/data/pricemulti?"
	else:
		base_url = "https://min-api.cryptocompare.com/data/pricemultifull?"
	
	fsyms_url = "fsyms={}".format(",".join(fsyms))
	tsyms_url = "tsyms={}".format(",".join(tsyms))
	
	# exchange specified
	if e != 'all':
		e_url = "e={}".format(e)
		url = "{}{}&{}&{}".format(base_url, fsyms_url, tsyms_url, e_url)
	else:
		url = "{}{}&{}".format(base_url, fsyms_url, tsyms_url)

	# http request
	r = requests.get(url)

	# decode to json
	data = r.json()
	
	#  select right format to return for full requests
	if full and format == 'raw':
		data = data['RAW']
	elif full and format == 'display':
		data = data['DISPLAY']

	return data


def get_latest_average(fsym, tsym, markets, format='raw'):
	"""
	Get the latest trading info of the requested pair as a volume weighted 
	average based on the markets requested.
	
	Args:
		fsym: FROM symbol.
		tsym: TO symbol.
		markets: List containing the market names.
		format: Default returns the 'RAW' format. Can be set to 'DISPLAY' 
			format.

	Returns:
		The returned latest average trading information dictionary contains
		the following key value pairs:
		{'PRICE': ...,
		 'LASTVOLUMETO': ...,
		 'TOSYMBOL': ...,
		 'LOW24HOUR': ...,
		 'CHANGE24HOUR': ...,
		 'FROMSYMBOL': ...,
		 'FLAGS': ...,
		 'VOLUME24HOUR': ...,
		 'HIGH24HOUR': ...,
		 'LASTUPDATE': ...,
		 'VOLUME24HOURT': ...,
		 'LASTMARKET': ...,
		 'CHANGEPCT24HOUR': ...,
		 'OPEN24HOUR': ...,
		 'MARKET': ...,
		 'LASTTRADEID': ...,
		 'LASTVOLUME': ...}
	"""
	base_url = "https://min-api.cryptocompare.com/data/generateAvg?"
	fsym_url = "fsym={}".format(fsym)
	tsym_url = "tsym={}".format(tsym)

	markets_url = "markets={}".format(",".join(markets))
	url = "{}{}&{}&{}".format(base_url, fsym_url, tsym_url, markets_url)

	# http request
	r = requests.get(url)

	# decode to json
	data = r.json()

	if format == 'raw':
		data = data['RAW']
	elif format == 'display':
		data = data['DISPLAY']

	return data


def get_day_average(fsym, tsym, e='all', avgType='HourVWAP', UTCHourDiff=0):
	"""
	


	"""
	pass






if __name__ == "__main__":

	# print("Examples get_coin_information()")
	# print("--------------------------------")
	# coin_data = get_coin_information(["BTC", "ETH"])
	# print(coin_data)
	# print()

	# coin_data = get_coin_information()
	# print(list(coin_data.keys())[:10])
	# print()

	# print("Examples get_latest_price()")
	# print("--------------------------------")
	# print(get_latest_price(["BTC"], ["EUR", "USD", "ETH"]))
	# print()

	# print(get_latest_price(["ETH"], ["EUR"], e="Kraken"))
	# print()

	# print(get_latest_price(["ETH", "BTC", "DASH"], ["EUR", "USD"]))
	# print()

	# print(get_latest_price(["ETH"], ["EUR", "BTC"], full=True))
	# print()

	# print(get_latest_price(["ETH"], ["EUR", "BTC"], full=True, format="display"))
	# print()

	print("Examples get_latest_average()")
	print("--------------------------------")
	print(get_latest_average("BTC", "USD", markets=["Poloniex"]))
	print()

	print(get_latest_average("BTC", "USD", 
	                         markets=["Poloniex", "Kraken", "Coinbase"], 
	                         format='display'))
	print()