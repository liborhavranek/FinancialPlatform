
# Pandas
# CZ: Importuji pandas jelikož potřebuji ukládat data do csv souboru
# ENG: Install pandas library for save data into csv file
import pandas as pd

# Datetime
# CZ: Pro práci s datumem a časem
# ENG: I will need work with date and with time
import datetime


# Requests
# CZ: Pro posílání dotazů
# ENG: for sending requests
import requests


# ConnectionError
# CZ: Toto bude aktivováno, pokud dojde k chybě připojení.
# ENG: This will be raised, if there is any connection error.
from requests.exceptions import ConnectionError

# BeautifulSoup
# CZ: Použiji pro webscraping pro získání dat už jsem v tom tvořil bota na hraní her
# ENG: I use this for webscrapping for gain data from web i have experience with create game bot
from bs4 import BeautifulSoup

# OS
# CZ: Pomůže mi identifikovat cesty pro uložení dat
# ENG: Help to me identify path for save data
import os


def web_content_div(web_content, class_path, value):
	web_content_div = web_content.find_all('div', {'class': class_path})
	try:
		if value != 'None':
			spans = web_content_div[0].find_all(value)
			texts = [span.get_text() for span in spans]
		else:
			texts = []
	except (IndexError):
		texts = []

	return texts


def real_time_price(stock_code):
	Error = 0
	url = f'https://finance.yahoo.com/quote/{stock_code}?p={stock_code}&.tsrc=fin-srch'
	try:
		r = requests.get(url)
		web_content = BeautifulSoup(r.text, 'lxml')
		# price nad price change
		texts = web_content_div(web_content, 'D(ib) Mend(20px)', 'fin-streamer')
		#print(texts)
		price, change, volume, latest_pattern, one_year_target = [], [], [], [], []

		if texts != []:
			price, change = texts[0], texts[1] + '' + texts[2]
		else:
			Error = 1
			price, change = [], []
		print(price, change)

	except (ConnectionError):
		price, change, volume, latest_pattern, one_year_target = [], [], [], [], []
		Error = 1
		print(ConnectionError)


	return price, change, volume, latest_pattern, one_year_target, Error



Stock = ['ES=F', 'AAPL']


while True:
	for stock_code in Stock:
		stock_price, change, volume, latest_pattern, one_year_target, Error = real_time_price(stock_code)
