import pandas as pd

def add_moving_average(data, window_size=7):
    """Adds moving average for the specified window size."""
    data[f'MA_{window_size}'] = data['Close'].rolling(window=window_size).mean()
    return data

