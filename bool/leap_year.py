def leap_year(year):
    if year % 400 == 0:   # leap year
        return True
    
    if  year % 100 == 0:    #not leap year
        return False
    
    if year % 4 == 0:         #leap year
        return True
    

    
    return False       #everything else not

print(leap_year(1997))
print(leap_year(2000))
print(leap_year(2100))
