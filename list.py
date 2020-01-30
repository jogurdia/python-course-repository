demo_list = [1, 'hello', 1.34, True, [1, 2, 3]] # in list we can use any data types
print(type(demo_list))
print(demo_list)
colors = ['red', 'green', 'blue']

# Result :

#JOGURDIA-M-X6MF:python-course jogurdia$ python list.py
#<type 'list'>
#[1, 'hello', 1.34, True, [1, 2, 3]]

r = list(range(1 , 11)) # range is use to create a list from 1st number to 2nd number x,y
print(r)

#Result :

#JOGURDIA-M-X6MF:python-course jogurdia$ python list.py
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(dir(r)) # we can also use dir to find what methods we can use

#JOGURDIA-M-X6MF:python-course jogurdia$ python list.py
#['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append'

print(len(demo_list)) # len is used to count objects on the list

print('red' in colors) # in is used to see if 'red' is inside list colors

print(colors)
colors[1] = 'black' # here we are telling python to change the position 1 in colors to black
print(colors)

#Result :

#JOGURDIA-M-X6MF:python-course jogurdia$ python list.py
#['red', 'green', 'blue']
#['red', 'black', 'blue']

colors.append('violet') # .append is used to add 1 element to the list
print(colors)

colors.extend(('rose', 'white')) # with .extend we can add more than 1 elements but inside list or tuple
print(colors)

print(colors)
colors.insert(1 , 'purple') # .insert will insert an element on the position given, this case 1
print(colors)

#JOGURDIA-M-X6MF:python-course jogurdia$ python list.py
#['red', 'black', 'blue', 'violet', 'rose', 'white']
#['red', 'purple', 'black', 'blue', 'violet', 'rose', 'white']

colors.pop() # pop is used to removed the last element from the list or based on index
print(colors)

colors.remove('red') # remove is used to removed the specified element from the list based on element name
print(colors)

#JOGURDIA-M-X6MF:python-course jogurdia$ python list.py
#['red', 'purple', 'black', 'blue', 'violet', 'rose', 'white']
#['red', 'purple', 'black', 'blue', 'violet', 'rose']
#['purple', 'black', 'blue', 'violet', 'rose'] 

colors.clear() # clear is used to delete all elements from the list
print(colors)

colors.sort() # sort is used to order elements based on alphabet 
print(colors) 

colors.sort(reverse=True) # sort is used to order elements based on inversed alphabet
print(colors)