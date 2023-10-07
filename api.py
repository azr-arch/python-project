from dhanhq import dhanhq

# Initialize the DhanHQ client
dhan = dhanhq("client_id", "access_token")

# Read stocks from a text file
with open('stocks.txt', 'r') as f:
    stocks = f.readlines()

# Loop through each stock
for stock in stocks:
    # Parse the stock data
    stock_data = stock.split(',')
    trigger_price = float(stock_data[1])
    stoploss = float(stock_data[2])
    target = float(stock_data[3])

    # Check if the current price meets the trigger price
    # For simplicity, let's assume we have a function that gets the current price
    current_price = get_current_price(stock_data[0])
    if current_price >= trigger_price:
        # Place an order
        dhan.place_order(
            security_id=stock_data[0],
            exchange_segment=dhan.NSE,
            transaction_type=dhan.BUY,
            quantity=1,
            order_type=dhan.MARKET,
            product_type=dhan.INTRA,
            price=current_price
        )

# Get the list of all orders for the day
orders = dhan.get_order_list()

# Print all orders
for order in orders:
    print(order)

