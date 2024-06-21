users = ['Dave', 'John', 'Sarah']

data = ['Dave', 42, True]

emptylist = [ ]

print("Dave" in emptylist)

print(users[0])   # first value in users
print(users[-1])   # last value in users

print(users.index('Sarah'))

print(users[0:2]) # first value through third value, but third/last value (Sarah) not shown
print(users[1:]) # everything in the list from 2nd value on

print(len(data))   # returns length of list (number of values)

users.append('Elsa')   # adding "Elsa" to list with append method
print(users)

users += ['Jason']   # adding "jason" to list using += (adding two lists together)
print(users)

users.extend(['Robert', 'Jimmy'])   # adding new users with extend method
print(users)

# users.extend(data)   #putting in just a list name with extend
# print(users)

users.insert(0, 'Bob')   #adding "Bob" the the very beginning of the list as first value 
print(users)

users[2:2] = ['Eddie', 'Alex']   # adding names to the second position (as second and third values)
print(users)

users[1:3] = ['Robert', 'PJ']   # puts robert in 1st position, PJ in third position
print(users)

# removing data from lists
users.remove('Bob')
print(users)

print(users.pop())   # returns last value in list
print(users)   # prints all values but last 

del users[0]   # using "delete" to get rid of values (del)
print(users)

data.clear()   # clears out all values, returns empty list
print(data)

# sorting lists
users.sort()
print(users)