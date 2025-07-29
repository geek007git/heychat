
import matplotlib.pyplot as plt

def plot_predictions(df, predictions):
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Close'], label='Actual Price')
    plt.plot(df.index, predictions, label='Predicted Price')
    plt.title("Stock Price Prediction")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
