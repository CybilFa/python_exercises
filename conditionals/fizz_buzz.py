def check_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        say =  "Fizz - buzz"
    
    elif num % 3 == 0:
        say =  "fizz"
    
    elif num % 5 == 0 :
        say = "buzz"
    
    else:
        say = str(num)
    
    return say

print(check_buzz(15))
print(check_buzz(13))