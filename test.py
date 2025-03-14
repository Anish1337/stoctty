import yfinance as yf
import time

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    stock_data = stock.history(period="1d") 
    return stock_data

def display_stock_data(symbol):
    all_stock_data = []
    
    while True:
        stock_data = get_stock_data(symbol)
        
        stock_row = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']].iloc[-1]
        
        all_stock_data.append(stock_row)
        
        print("\033c", end="")
        
        print(f"Live Stock Data for {symbol} (Updated Every 60 Seconds):")
        
        for row in all_stock_data:
            print(row)
        
        time.sleep(5)  

if __name__ == "__main__":
    symbol = "NVDA"
    display_stock_data(symbol)

