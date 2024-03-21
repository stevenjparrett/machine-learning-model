# src/data_fetcher.py
import yfinance as yf

def fetch_stock_data(ticker, period='1mo'):
    """Fetches historical stock data for the given ticker."""
    data = yf.download(ticker, period=period)
    print(f"fetched data for {ticker}: {data.head()}")
    return data
