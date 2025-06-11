#1. 
def insert_underscores(txt):
    vowels = 'aeiouAEIOU'
    result = ''
    count = 0
    i = 0

    while i < len(txt):
        result += txt[i]
        count += 1

        # Har 3-belgidan keyin tekshir
        if count == 3:
            if i + 1 < len(txt):  # Oxiriga yetmagan bo‘lsa
                if txt[i] in vowels or txt[i+1] == '_':
                    # Unli yoki _ bor – keyingi belgigacha suramiz
                    j = i + 1
                    while j < len(txt) and (txt[j] in vowels or txt[j] == '_'):
                        result += txt[j]
                        i += 1
                        j += 1
                    if j < len(txt) - 1:  # Oxirida bo‘lmasa
                        result += '_'
                else:
                    result += '_'
            count = 0
        i += 1

    # Oxirida bo‘lsa, `_` olib tashlaymiz
    if result.endswith('_'):
        result = result[:-1]
    return result

#2.
n= int(input('Please, enter a number: '))
for i in range(n):
    print(i**2)

#3
i=1
while i <=10:
    print(i)
    i+=1

#3.2
rows = 5  # nechta qatorgacha yozamiz

for i in range(1, rows + 1):  # 1 dan 5 gacha
    for j in range(1, i + 1):  # har bir qatorda 1 dan i gacha
        print(j, end=' ')  # bitta qator ichida chiqaramiz
    print()  # har qator tugaganda yangi qatorga o‘tamiz

#3.
n=int(input('Please, enter a number: '))
total= sum(range(1, n+1))
print(total)

num=int(input('Please, enter a number: '))
for i in range(1, 11):
    print(num*i)
#4.
num=int(input('Please, enter a number: '))
for i in range(1, 11):
    print(num*i)


#5.
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num >500:
        break 
    if num >100:
        print(num)


#6.
num=int(input('Please, enter a number: '))
digit_count = len(str(abs(num)))
print('total digits:', digit_count)


#7.
n = 5  

for i in range(n, 0, -1):  
    for j in range(i, 0, -1):
        print(j, end=' ')  
    print()

#8
list1= [10, 20, 30, 40, 50]
for i in range(len(list1) -1, -1,-1):
    print(list1[i])


#9.
for i in range(-10, 0):  # -10 dan 0 gacha (0 kirmaydi)
    print(i)

#10.
for i in range(5):  # 0 dan 4 gacha (5 kirmaydi)
    print(i)

print("Done!")


#11.
start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break  # tub emas
        else:
            print(num)


#12.
# Nechta element chiqaramiz
n = 10

# Dastlabki ikkita son
a, b = 0, 1

print("Fibonacci sequence:")

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b  # keyingi sonlarni hisoblash


#13.
n = int(input("Enter a number: "))  # foydalanuvchidan son olish

factorial = 1  # boshlang'ich qiymat

for i in range(1, n + 1):
    factorial *= i  # faktorialga i ni ko'paytiramiz

print(f"{n}! = {factorial}")



