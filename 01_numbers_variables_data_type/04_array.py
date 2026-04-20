import array as arr

my_array = arr.array("i", [1, 2, 3, 4, 5, 5])
print(type(my_array), my_array)

print(my_array[0])
print(my_array.itemsize)
my_array.append(6)
print(my_array)
my_array.pop()
print(my_array)
