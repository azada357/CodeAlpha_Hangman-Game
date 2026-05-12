#✅ TASK 2: Stock Portfolio Tracker 
#● Goal: Build a simple stock tracker that calculates total investment based on manually defined stock prices. 
#● Simplified Scope:
# ○ User inputs stock names and quantity. 
# ○ Use a hardcoded dictionary to define stock prices (e.g., {"AAPL": 180, "TSLA": 250}). ○ Display total investment value and optionally save the result in a .txt or .csv file. 
# ● Key Concepts Used: dictionary, input/output, basic arithmetic, file handling (optional). 
# My dictionary
import csv
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300
}

stock = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock in stock_prices:
    price = stock_prices[stock]
    total = price * quantity
    print("Total investment:", total)
else:
    print("Stock not found")

portfolio = {}  # --->

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        if stock in portfolio:
            portfolio[stock] = portfolio[stock] + quantity
        else:
            portfolio[stock] = quantity

    else:
        print("Stock not found")

total_value = 0

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock}: {quantity} shares = {value}")

print("Total Portfolio Value:", total_value)


with open("Portfolio.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Value"])

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        writer.writerow([stock, quantity, value])
