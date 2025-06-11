#1. 
students = {
"Jack": 80, 
"John": 75,
"Bob": 90,
"Jasur": 55}
sorted_asc = dict(sorted(students.items(), key=lambda x: x[1]))
sorted_desc = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))
print(sorted_asc)
print(sorted_desc)

#2.
dict1= {0: 10, 1: 20}
dict1[2]=30
print(dict1)

#3.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = dic1| dic2| dic3
print(dic4)

#4.
n=int(input("n ni kiritng: "))
dic1={x: x*x for x in range (1, n+1)}
print(dic1)

#5. 
dic1={x: x*x for x in range (1, 16)}
print(dic1)

# Set Exercises
# 1. Create a Set

my_set = {1, 2, 3, 4, 5}
print(my_set)


# 2. Iterate Over a Set
my_set = {1, 2, 3, 4, 5}
print("set elementlari:")
for item in my_set:
    print(item)

#3. Add Member(s) to a Set
my_set = {1, 2, 3, 4, 5}
my_set.update  ([6, 7])
print(my_set)

#4. Remove Item(s) from a Set
my_set = {1, 2, 3, 4, 5, 6, 7}
my_set.remove(5)
print(my_set)

#5. Remove an Item if Present in the Set
my_set = {1, 2, 3, 4, 5, 6, 7}
item = 4
if item in my_set:
    my_set.remove(item)
    print(f'{item} has been removed from my_set')
else:
    print(f'{item} is not found')
print(my_set)
