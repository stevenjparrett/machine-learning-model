import yfinance as yf

def fetch_stock_data(tickers, start_date, end_date):
    """Fetches historical stock data for given tickers from Yahoo Finance."""
    data = yf.download(tickers, start=start_date, end=end_date)
    return data
