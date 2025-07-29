
from model.predictor import predict_stock
from data.stock_fetcher import fetch_stock_data
from utils.plot_utils import plot_predictions

def main():
    print("\n📈 Stock AI Predictor\n")
    ticker = input("Enter stock ticker (e.g., AAPL, TSLA): ").upper().strip()

    print("\n🔍 Fetching stock data...")
    df = fetch_stock_data(ticker)

    if df is None or df.empty:
        print(f"❌ Failed to fetch data for {ticker}. Check the symbol and try again.")
        return

    print("\n🤖 Predicting stock prices...")
    predictions = predict_stock(df)

    print("\n📊 Plotting results...")
    plot_predictions(df, predictions)

if __name__ == "__main__":
    main()
