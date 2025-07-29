
def predict_stock(df):
    import numpy as np
    # Dummy prediction: shift 'Close' column by 1 day
    predictions = df['Close'].shift(-1).fillna(df['Close'].iloc[-1])
    return predictions
