from keras.models import Sequential
from keras.layers import LSTM, Dense

def build_model(input_shape):
    """Builds a simple LSTM model."""
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        LSTM(50),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_model(model, X_train, y_train, epochs=10, batch_size=32):
    """Trains the model."""
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)
