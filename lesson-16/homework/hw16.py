# 1. Convert List to 1D Array
import numpy as np
l1 = [12.23, 13.32, 100, 36.32] 

arr1 = np.array(l1)
arr1


# 2. Create 3x3 Matrix (2?10)

arr2= np.array([
    np.arange(2, 5), 
    np.arange(5, 8), 
    np.arange(8, 11)
])
arr2


# 3. Null Vector (10) & Update Sixth Value
arr3 = np.zeros(10)
arr3[7] = 11
arr3

# 4. Array from 12 to 38
arr4 = np.arange(12, 38)
arr4

# 5. Convert Array to Float Type
l1= [1, 2, 3, 4]
arr5_array = np.array(l1)

arr5_float = arr5_array.astype(float)
#type(arr5_float)
#print(arr5_array)
print(arr5_float)

#6. 

celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])

fahrenheit = celsius * 9 / 5 + 32

print("Values in Centigrade degrees:")
print(np.round(celsius, 2))

print("\nValues in Fahrenheit degrees:")
print(np.round(fahrenheit, 2))

#7. Append Values to Array (Do self-tudy) 
array_org = np.array([10, 20, 30])
l1 = list(map(int, input("Raqamlarni kiriting (masalan: 40 50 60): ").split()))
array_new = np.array(l1)
new_array = np.append(array_org, array_new)
new_array

#8. Array Statistical Functions (Do self-tudy)
arr8 = np.random.randint(0, 100, size=10)
arr8
mean1 = np.mean(arr8)
median1 = np.median(arr8)
standat_deviation1 = np.std(arr8)


#9 Find min and max
array_10x10 = np.random.rand(10, 10)
array_10x10
min_array = np.min(array_10x10)
max_array = np.max(array_10x10)
min_array
max_array

# 10 Create a 3x3x3 array with random values.
array_3x3x3 = np.random.rand(3, 3, 3)
array_3x3x3



