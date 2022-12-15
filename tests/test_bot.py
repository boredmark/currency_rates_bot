import sys
sys.path.append('/Users/valentyn/Documents/my_projects/bot_exchange_rates')
import bot


def test_dict():
    b = bot.Bot('1')
    assert b.processed_massage({'last_massage_text': '/currency_list'}) is True
