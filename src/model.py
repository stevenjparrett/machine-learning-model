# src/model.py
from .data_fetcher import fetch_stock_data

# In model.py
def predict_next_day_close(ticker):
    data = fetch_stock_data(ticker, period='5d')
    if not data.empty:
        last_close = round(data['Close'].iloc[-1], 2)
        print(f"Last close price for {ticker}: {last_close}")  # Confirm the last close price
        return last_close
    else:
        print(f"No data fetched for {ticker}.")  # Indicate no data was fetched
        return None
