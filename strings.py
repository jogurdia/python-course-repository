my_str = "Hello World"

# print(dir(my_str)) = We can use dir(<variable>) to see what attributes we have for that string

print(my_str.upper()) # Upper to convert all the string to upper case
print(my_str.lower()) # Lower to convert all the string to lower case
print(my_str.swapcase()) # Swapcase to swap the string to uppper or lower letters
print(my_str.capitalize()) # Capitalized to user upper case on the first letter of the string
print(my_str.replace('Hello' , 'Bye')) # Replace to replace a string by other string
print(my_str.replace('Hello' , 'Bye').upper()) # We can use a attributes after other method 
print(my_str.count('l')) # Count is used to count how many carateres of l are on the string
print(my_str.startswith('Hello')) #Startswith is used to see if the string start with ...
print(my_str.endswith('World')) # endswith is used to see if the string end with ...
print(my_str.split()) # split is used to separate strings, by default it separate by space between the string
print(my_str.split(',')) # split used to separate string based on ,
print(my_str.find('o')) # find is used to see on what location is found the o abd the string stars with 0
print(len(my_str)) # len is used to count how many characters we have on the string
print(my_str.index('e')) # index is to find the location of the data in the string
#print(my_str.isnumeric()) # isnumeric is used to print if the string is numeric or not
print(my_str.isalpha()) # isalpha is used to print if string is alfhanumeric or not

print("My name is " + my_str) # we can concatenate string + variable
#print(f"My name is {my_str}")
print("My name is {0}".format(my_str))

