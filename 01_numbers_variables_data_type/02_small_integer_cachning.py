# int: immutable data type
a = 1000
b = a
print(id(a), id(b))
print(type(a))

a = 0
print(id(a), id(b))

# small integer caching
# -5..256
# small integers are cached by Python, so they point to the same memory location
# small integer cachning works in terminal mode
# if you run the whole file the interpreter may optimize the code and create only one object for small integers
a = 100
b = 100
print(id(a), id(b))
