import sys
sys.path.append('/Users/valentyn/Documents/my_projects/bot_exchange_rates')
import bot



def test_bot_processed_massage_sell_code():
    expect = "You want to sell United States Dollar, text the amount that you want to sell\nExample: 100, 123, 10500\nor /reset"
    assert bot.Bot('1').processed_massage({'last_massage_text': 'USD'}) == expect



def test_bot_processed_massage_start():
    expect = "Text three-letter currency code which you want to sell\nExample: USD, EUR, GBP"
    assert bot.Bot('1').processed_massage({'last_massage_text': '/start'}) == expect



def test_bot_processed_massage_amount_valid():
    b = bot.Bot('1')
    b.sell_flag = True
    expect = 'Incorrect amount'
    assert b.processed_massage({'last_massage_text': 'dfgdfg'}) == expect
