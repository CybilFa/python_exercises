# check whether a number is armstrong or not
# sum each digit raised to power num of digits

def is_armstrong(number):
    digits = str(number)
    num_digits = len(digits)

    total = sum(int(digit) ** num_digits for digit in digits)
    return total == number  #true/false



print('test1', is_armstrong(153))
print('test2', is_armstrong(136))