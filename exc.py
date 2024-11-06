

prices = list(map(int, input("Enter stock price in several days: ").split()))

#search for the max price and min price 
#then substract them and get profit 
def max_profit(prices):
  
    max = prices[0]
    min = prices[0]

    for price in prices:
        if price > max:
            max = price

        if price < min:
            min = price

    profit = max - min
    return profit
  
print("Max profit is ",max_profit(prices))