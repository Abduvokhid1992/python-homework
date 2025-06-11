#1.
fruits = ['olma', 'anor', 'shaftoli', 'gilos', 'nok']
print(fruits[2])

#2.
a=[1, 2, 3]
b=[4, 5, 6]
c=a+b
print(c)

#3.
a=[1, 2, 3, 4, 5, 6, 7, 8]
firs=a[0]
middle=len(a)//2
last=a[-1]
new_a=[firs, middle, last]
print(new_a)

#4. 
favorite_movies=["O'tgan Kunlar", "Shum bola", "Prison break", "Interstellar", "Kurtlar Vadisi"]
movies_tuple = tuple(favorite_movies)
print(favorite_movies)
print(movies_tuple)

#5.
cities= ["Toshkent", "Paris", "New York", "Buxoro", "Nukus"]
if "Paris" in cities:
    print("Paris is in the list")
else:
    print("Paris is not in the list")

#6.
numbers=[1, 2, 3, 4, 5]
dub_numbers=numbers * 2
print(dub_numbers)

#7.
numbers=[1, 2, 3, 4, 5]
numbers[0], numbers[4] = numbers[-1], numbers[0]
print(numbers)

#8. 
numbers = tuple(range(1,11))
new_numbers = numbers[3:7]

print(new_numbers)

#9.
colours= ['red', 'blue', 'yellow', 'blue', 'green', 'blue', ' black']
count=colours.count('blue')
print(count)

#10. 
animals=('dog', 'cat', 'pig', 'lion', 'snake')
index_of_lion=animals.index('lion')
print(index_of_lion)

#11.
a=(1, 2, 3)
b=(4, 5, 6)
c= a + b
print('added tuples', c)

#12
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tuple = ('olma', 'anor', 'shaftoli', 'gilos', 'nok')
lenth_list=len(list)
lenth_tuple = len(tuple)
print(lenth_list)
print(lenth_tuple)

#13.
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
numbers_list = list(numbers_tuple)
print(numbers_tuple)
print(numbers_list)

#14. 
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90)
max=max(numbers)
min=min(numbers)
print(max)
print(min)


#15.
tuple = ('olma', 'anor', 'shaftoli', 'gilos', 'nok')
reverse_tuple = tuple[::-1]
print(reverse_tuple)
