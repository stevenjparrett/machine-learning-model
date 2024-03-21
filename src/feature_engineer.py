import pandas as pd

def handle_missing_values(data):
    """Handles missing values by forward filling."""
    data.fillna(method='ffill', inplace=True)
    return data

def add_moving_average(data, window_size=7):
    """Adds moving average for the specified window size."""
    data[f'MA_{window_size}'] = data['Close'].rolling(window=window_size).mean()
    return data

def preprocess_data(data):
    """Preprocesses the data by handling missing values and adding moving averages."""
    data = handle_missing_values(data)
    data = add_moving_average(data)
    return data
