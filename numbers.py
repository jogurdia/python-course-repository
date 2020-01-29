10 #integer
15.5 #float

print(type(9))
print(type(10.5))

#Result :

#JOGURDIA-M-X6MF:python-course jogurdia$ python numbers.py
#<type 'int'>
#<type 'float'>

3 + 1
2 - 1
5 * 6
6 / 2
2**3 # this is exponential 2^3
3 // 2 # this is called module and is used to get just the integer value and not the float 
20 - 10 / 5 * 3**2 # will follow the same rule of order doing the operation
(20 - 10) / (5 * 3**2) # we can make maths using () as well 

age = input("Insert your age :") # input is used to ask the user to enter the value, will be str
print(age)

age = input("Insert your age :")
print(type(age))
new_age = age + 10
print(new_age)

age = input("Insert your age :")
new_age = int(age) + 5 # int is used to convert str age to integer, will only convert str "10" to 10 
print(new_age)
