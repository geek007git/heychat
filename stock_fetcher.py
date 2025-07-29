
import yfinance as yf

def fetch_stock_data(ticker):
    try:
        data = yf.download(ticker, period="6mo", interval="1d")
        return data
    except Exception as e:
        print("Error fetching data:", e)
        return None
