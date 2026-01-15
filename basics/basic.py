# name_assignment
var1 = 2
var2 = 3

print(type(var1))  #<class 'int'>
print(var2) #3
var2 = 4

print(var2) #4

def add_two_nums(num1, num2):
    total = num1 + num2
    return total

print('Total of two numbers:', add_two_nums(3, 4))