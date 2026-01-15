def steps(number):
    if number < 1:       #if number is negative raise value error
        raise ValueError("given number is not a positive integer")
    counter = 0            #to count how many steps it takes to reach 1
    
    while number != 1:  #repeat until number is not 1
        if number % 2 == 0:        #if remainder 0 its even
            number //= 2     
        else:
            number = (number * 3) + 1          #odd number
        counter += 1                          # increment counter
    return counter

print(steps(15))
print(steps(12))