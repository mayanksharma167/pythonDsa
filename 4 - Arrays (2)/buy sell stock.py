#buy and sell stocks
stocks_prices = [7,1,5,3,6,4]

def buy_sell_stock(prices):
    buy_price = float("inf")
    max_profit = 0
    for i in range(0, len(prices)):
        # CASE 1: PROFIT (Buy price is less than sell price)
        if buy_price < prices[i]:
            profit = prices[i] - buy_price
            max_profit = max(max_profit,profit)
        else:
            buy_price = prices[i]

    return max_profit

print(buy_sell_stock(stocks_prices))