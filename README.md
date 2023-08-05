# Stock-Price-Program


This Python project enables the analysis of stock prices for two different stocks - Stock A and Stock B. It includes functions to process stock data, calculate the ratio of stock prices, and output the results.

## Purpose

The purpose of this project is to process the data feed of Stock A and Stock B's price to enable users to analyze when trading for the stock should occur.

## Functionality

The project consists of the following functions:

### `getDataPoint`

This function takes a dictionary containing stock data and returns a tuple of stock name, bid price, ask price, and calculated price (average of bid and ask prices).

### `getRatio`

This function takes data for two stocks (Stock A and Stock B) and calculates the ratio of their prices.

### `main`

The main function initializes sample stock data for Stock A and Stock B, calls the other two functions, and then outputs the results.

## Acceptance Criteria

- `getDataPoint` function should return the correct tuple of stock name, bid_price, ask_price, and price.
- `getRatio` function should return the ratio of the two stock prices.
- `main` function should output correct stock info, prices, and ratio.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the Python script using the command: `python stock_price_analysis.py`

## Sample Data

The script uses sample stock data for Stock A and Stock B as follows:

```python
stock_A_data = {'name': 'Stock A', 'bid': 100, 'ask': 105}
stock_B_data = {'name': 'Stock B', 'bid': 80, 'ask': 85}
