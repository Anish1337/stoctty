import yfinance as yf

def get_stock_data(symbol):
    # Fetch the stock data using yfinance
    stock = yf.Ticker(symbol)
    stock_data = stock.history(period="1d")  # Get stock data for the past day
    return stock_data

def display_stock_data(symbol):
    stock_data = get_stock_data(symbol)
    
    # Display the stock data in a readable format
    print(f"Stock Data for {symbol}:")
    print(stock_data[['Open', 'High', 'Low', 'Close', 'Volume']])

if __name__ == "__main__":
    # The stock symbol for NVIDIA is 'NVDA'
    symbol = "NVDA"
    display_stock_data(symbol)

