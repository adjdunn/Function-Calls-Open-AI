#Test functions


def get_stock_price(symbol):
    """
    Retrieve the stock price for a given symbol.
    """
    stock_prices = {
        'MSFT': 420,
        'NVDA': 120,
        'AMZN': 60,
        'AAPL': 150
    }
    
    # Check if the symbol is in the stock_prices dictionary
    if symbol in stock_prices:
        price = stock_prices[symbol]
    else:
        price = 1000  # Default price if symbol is not found

    return price



def get_weather(location, units='c'):
    """
    Retrieve the weather temperature for a given location.
    """
    # Determine the temperature based on the units
    if units == 'c':
        temp = 25  # Temperature in Celsius
    else:
        temp = 75  # Temperature in Fahrenheit

    return temp
