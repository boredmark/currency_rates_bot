from bot import Bot
import time

token = '5716630458:AAEeV_f_YMNrXErLl80VbZxpUkT4o2BRwfM'
bot = Bot(token)

def bot_polling():
	last_massage_id = 0
	while True:
		info = bot.get_info()
		if info['massage_id'] > last_massage_id:
			massage_to_send = bot.processed_massage(info)
			bot.send_massage(info, massage_to_send)
		last_massage_id = info['massage_id']
		time.sleep(1)		


if __name__ == '__main__':
	while True:
		try:
			bot_polling()
		except Exception as e:
			continue
