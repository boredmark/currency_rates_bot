import requests
from python_currency_dict import currency_list

class Bot:

	def __init__(self, token):
		self.token = token
		self.sell_flag = False
		self.amount_flag = False
		self.buy_flag = False
		self.sell_code = ''
		self.amount_to_sell = ''
		self.buy_code = ''
 
	def get_bot_updates(self):
		url = f'https://api.telegram.org/bot{self.token}/getUpdates'
		request = requests.get(url)
		return request.json()['result']

	def get_info(self):
		info = self.get_bot_updates()
		last_massage_text = info[-1]['message']['text']
		chat_id = info[-1]['message']['chat']['id']
		massage_id = info[-1]['message']['message_id']
		return {'last_massage_text': last_massage_text, 'chat_id': chat_id, 'massage_id': massage_id}

	def send_massage(self, info: dict, massage_to_send):
		url = f'https://api.telegram.org/bot{self.token}/sendMessage'
		request = requests.post(url, data={'chat_id': info['chat_id'], 'text': massage_to_send})
		return 'massage successfully sent'
	
	def get_exchange_rate(self, sell_symbol, buy_symbol, amount): 
		url = f'https://api.exchangerate.host/latest?base={sell_symbol}&symbols={buy_symbol}&amount={amount}&places=2'
		request = requests.get(url)
		data = request.json()
		result = {
			'sell_symbol': sell_symbol, 
			'buy_symbol' :buy_symbol,
			'amount_to_sell' : amount,
			'amount_to_buy': data['rates'][f'{buy_symbol}']
		}		
		return result


	def processed_massage(self, info: dict):

		if self.sell_flag is False and self.amount_flag is False and self.buy_flag is False and info['last_massage_text']not in ['/reset', '/start']:
			if info['last_massage_text'].upper() in currency_list.keys():
				self.sell_flag = True
				self.sell_code = info['last_massage_text'].upper()
				print('creating sell code')
				return f"You want to sell {currency_list[self.sell_code]}, text the amount that you want to sell\nExample: 100, 123, 10500\nor /reset"
			else:
				print('sell code error')
				return 'Incorrect three-letter code\nText three-letter currency code which you want to buy\nExample: USD, EUR, GBP'


		if info['last_massage_text'] in ['/reset', '/start']:
			self.sell_flag = False
			self.amount_flag = False
			self.buy_flag = False
			print('reset flags')
			return 'Text three-letter currency code which you want to sell\nExample: USD, EUR, GBP'

		if self.sell_flag is True and self.amount_flag is False and self.buy_flag is False:
			if info['last_massage_text'].isdigit():
				self.amount_flag = True
				self.amount_to_sell = info['last_massage_text']
				print('create amount')
				return f"You want to sell {self.amount_to_sell} {currency_list[self.sell_code]}\nText three-letter currency code which you want to buy\nExample: USD, EUR, GBP\nor /reset"
			else:
				print('error amount')
				return "Incorrect amount\ntext the amount that you want to sell\nExample: 100, 123, 10500"

		if self.sell_flag is True and self.amount_flag is True and self.buy_flag is False:
			if info['last_massage_text'].upper() in currency_list.keys():
				self.buy_flag = True
				self.buy_code  = info['last_massage_text'].upper()
				print(f'Starting external api function {self.amount_to_sell},{self.sell_code},{self.buy_code}')
				result = self.get_exchange_rate(self.sell_code, self.buy_code, self.amount_to_sell)
				print(result)
				return f"{result['amount_to_sell']} {currency_list[result['sell_symbol']]} --- {result['amount_to_buy']} {currency_list[result['buy_symbol']]}\n/start or /reset to count again"
			else:
				return 'Incorrect three-letter code\nText three-letter currency code which you want to buy\nExample: USD, EUR, GBP'

		if self.sell_flag is True and self.amount_flag is True and self.buy_flag is True:
			return '/start or /reset to count again'










		




