
# 1. Estimate value after exchange
def exchange_money(budget, exchange_rate):
    """Calculate currency in pkr from dollar"""
    
    return budget / exchange_rate

print('Exchange money', exchange_money(127.5, 1.2))
# 2. Calculate currency left after an exchange

def get_change(budget, exchanging_value):
    return budget - exchanging_value

print('GET THE CHANGE: ', get_change(127.5, 120))

#3. calculate value of bills

def get_value_bills(denomination, num_of_bills):
    total_val = num_of_bills * denomination
    return total_val

print("Total value of bills", get_value_bills(10, 3))

#4.calculate number of bills

def get_num_of_bills(amount, denomination):
    currency_bills = int(amount // denomination)
    return currency_bills
print('Currency bills:', get_num_of_bills(127.5, 5))

#5. Calculate leftover after exchanging into bills
def get_leftover_bills(amount, denomination):
    leftover =  amount % denomination   #leftover money that cannot be payed for bills
    return leftover

print(' Left over of bills: ', get_leftover_bills(127.5, 20))

# 6. Calculate value after exchange

def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread_decimal = 10/100
    value_exchange = exchange_rate + (exchange_rate * spread_decimal)
    foreign_money = budget / value_exchange
    return int(foreign_money // denomination * denomination)

print ('Exchangeable value', exchangeable_value(127.25, 1.20, 10, 20))
print ('Exchangeable value', exchangeable_value(127.25, 1.20, 10, 5))



   

