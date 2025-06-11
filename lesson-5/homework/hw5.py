#1.
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError ('Year must be an integer')
    return(year % 4 == 0 and year % 100 != 0) or (year % 400 ==0)

year=2024
if is_leap(year):
    print(f'{year} is leap year')
else:
    print(f'{year} is not leap year') 

#2.
#Conditional Statements Exercise
n = int(input('Please, enter a number: '))
if n % 2 == 1:
    print('Weird')
else:
    if 2 < n <=5:
        print('Not Weird')
    elif 6 <= n <= 20:
        print('Weird')
    else: 
        print('Not Weird')
