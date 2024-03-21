import matplotlib.pyplot as plt

def plot_predictions_vs_actual(actual, predictions):
    """Plots the actual vs. predicted stock prices."""
    plt.figure(figsize=(10, 6))
    plt.plot(actual, color='blue', label='Actual')
    plt.plot(predictions, color='red', alpha=0.7, label='Predicted')
    plt.title('Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()
