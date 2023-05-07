import os
import yfinance as yf
from apscheduler.schedulers.blocking import BlockingScheduler

def get_prices(tickers):
	prices = []
	for ticker in tickers:
		ticker = yf.Ticker(ticker)
		history = ticker.history(period="1h")
		close = history['Close'][0]
		prices.append(close)
	return prices
	
def get_ratio(prices):
	ratio = round(prices[1] / prices[0], 2)
	return ratio

def send_notify(title, message):
    os.system('notify-send "'+title+'" "'+message+'"')

def main():
    tickers = ['USD=X', 'AMD=X']
    prices = get_prices(tickers)
    ratio = get_ratio(prices)
    send_notify('1 US Dollar equals', str(ratio)+' Armenian Dram\n')

if __name__ == '__main__':
	main()
	scheduler = BlockingScheduler()
	scheduler.add_job(main, 'interval', hours=12)
	scheduler.start()
