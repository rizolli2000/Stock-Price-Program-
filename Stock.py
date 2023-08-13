def getDataPoint(stock_data):
    """
    Function to process stock data and return a tuple of stock name, bid_price, ask_price, and price.

    Parameters:
        stock_data (dict): A dictionary containing stock data with keys 'name', 'bid', and 'ask'.

    Returns:
        tuple: A tuple containing stock name, bid_price, ask_price, and price.
    """
    stock_name = stock_data['name']
    bid_price = stock_data['bid']
    ask_price = stock_data['ask']
    price = (bid_price + ask_price) / 2
    return stock_name, bid_price, ask_price, price

def getSpread(stock_data):
    """
    Function to calculate the spread between bid and ask prices.

    Parameters:
        stock_data (dict): Stock data in the form of a dictionary.

    Returns:
        float: The spread between bid and ask prices.
    """
    bid_price = stock_data['bid']
    ask_price = stock_data['ask']
    spread = ask_price - bid_price
    return spread

def getRatio(stock_data_A, stock_data_B):
    """
    Function to calculate the ratio of two stock prices.

    Parameters:
        stock_data_A (dict): Stock A data in the form of a dictionary.
        stock_data_B (dict): Stock B data in the form of a dictionary.

    Returns:
        float: The ratio of stock A price to stock B price.
    """
    _, _, _, price_A = getDataPoint(stock_data_A)
    _, _, _, price_B = getDataPoint(stock_data_B)
    ratio = price_A / price_B
    return ratio

def analyzeRatio(ratio, threshold=1.2):
    """
    Function to analyze the ratio and provide a recommendation based on a threshold.

    Parameters:
        ratio (float): The ratio of stock A price to stock B price.
        threshold (float): Threshold for ratio comparison. Default is 1.2.

    Returns:
        str: Recommendation message based on the comparison.
    """
    if ratio > threshold:
        return "Stock A is overpriced compared to Stock B. Consider selling Stock A and buying Stock B."
    elif ratio < 1 / threshold:
        return "Stock B is overpriced compared to Stock A. Consider selling Stock B and buying Stock A."
    else:
        return "The ratio is within an acceptable range. No immediate action is recommended."

def main():
    # Sample stock data for stock A and stock B
    stock_A_data = {'name': 'Stock A', 'bid': 100, 'ask': 105}
    stock_B_data = {'name': 'Stock B', 'bid': 80, 'ask': 85}

    # Get data points for stock A and stock B
    stock_A_info = getDataPoint(stock_A_data)
    stock_B_info = getDataPoint(stock_B_data)

    # Calculate the ratio of stock A to stock B prices
    ratio = getRatio(stock_A_data, stock_B_data)

    # Calculate the spread for stock A and stock B
    spread_A = getSpread(stock_A_data)
    spread_B = getSpread(stock_B_data)

    # Analyze the ratio and provide a recommendation
    recommendation = analyzeRatio(ratio)

    # Output the results
    print(f"Stock A Info: Name: {stock_A_info[0]}, Bid Price: {stock_A_info[1]}, Ask Price: {stock_A_info[2]}, Price: {stock_A_info[3]}, Spread: {spread_A}")
    print(f"Stock B Info: Name: {stock_B_info[0]}, Bid Price: {stock_B_info[1]}, Ask Price: {stock_B_info[2]}, Price: {stock_B_info[3]}, Spread: {spread_B}")
    print(f"Ratio of Stock A to Stock B prices: {ratio}")
    print(recommendation)

if __name__ == "__main__":
    main()

