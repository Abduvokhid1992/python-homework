#1. 
ism=(input("Please, enter your age: "))
year_of_birth = int(input("Please, enter year of your birth: "))
now = 2025
age = now - year_of_birth
print(f'Hello {ism}, your are {age} years old.')
# 2.
car_brands = ["Tesla", "Audi", "BMW", "Mazda", "Subaru", "Toyota", "lexus", "Nissan", "Kia", "Ford", "chevy", "Honda"]
txt = 'MsaatmiazD'
txt_lower = txt.lower()
found_cars = []
for brand in car_brands:
    brand_lower = brand.lower()
    temp_txt = list(txt_lower)
    match = True
    for char in brand_lower:
        if char in temp_txt:
            temp_txt.remove(char)
        else:
            match = False
            break

    if match:
        found_cars.append(brand)
print(found_cars)
#3.
car_brands = ["Matiz", "Audi", "BMW", "Mazda", "Subaru", "Toyota", "lexus", "Nissan", "Kia", "Ford", "chevy", "Honda"]
txt = 'MsaatmiazD'
txt_lower = txt.lower()
found_cars = []
for brand in car_brands:
    brand_lower = brand.lower()
    temp_txt = list(txt_lower)
    match = True
    for char in brand_lower:
        if char in temp_txt:
            temp_txt.remove(char)
        else:
            match = False
            break

    if match:
        found_cars.append(brand)
print(found_cars)
#4.
txt = "I'am John. I am from London"
words = txt.split()
if "from" in words:
    index = words.index("from")
    if index +1 <len(words):
        residence_area = words[index+1]
    else:
        residence_area = "Not Found"
else:
    residence_area = "Not Found"

print(residence_area)

#5.
matn = input("Please enter a words")
a=matn[::-1]
print(a)

#6.
text=input("Please enter a text: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for letter in text:
    if letter in vowels:
        vowel_count += 1
print("number of vowels:", vowel_count)

#7. 
numbers=input("Please enter number with comma ")
numbers_list=[int(a.strip()) for a in numbers.split(',')]
max_number = max(numbers_list)
print(max_number)

#8.
matn = input("Please enter a words")
matn = matn.lower()
a=matn[::-1]
if matn == a:
    print("this word is a palindrom")
else:
    print("thi sword is  not a palindrom")

#9. 
email = input("Please enter an email address")
split = email.split('@')
if len(split) == 2:
    domen = split[1]
    print("Domen of the email:", domen)
else:
    print("You entered wrong email address")
