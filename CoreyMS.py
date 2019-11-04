#source https://www.youtube.com/watch?v=C-gEQdGVXbk

print()
condition = False
#long version
""" if condition:
    x=1
else:
    x=0 """

#Ternary Conditionals 
x = 1 if condition else 0
print ("Trick 1 result is ",x)
print()

########
num1 = 10_000_000_000
num2 = 100_000_000

result = num1+num2
print(result)


#or better way
print("Trick 2 result is ", f'{result:,}')


#Trick number 3
""" 
with open('test.txt') as f:
    file_content = f.read()
end 
"""



#Trick number 4
names =['Corey', 'Chris', 'Dave', 'Travis']
print("Trick number 4")
for index, name in enumerate(names, start=1):
    print(index,name)
print()

#Trick number 5
names =['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes =['Spiderman', 'Superman', 'Deadpool', 'Batman']
unverses = ['Marvel', 'DC', 'Marvel', 'DC']
print("Result of Trick number 5")
for name, hero, universe in zip(names, heroes, unverses):
    print(f'{name} is actually {hero} from {universe}')
print()
print('unpacked version')  
for value in zip(names, heroes, unverses):
    print(value)

print()

#Trick number 6
a, b, *c = (1, 2, 3, 4, 5, 6)
#or
a, b, *_ = (1, 2, 3, 4, 5, 6)

print(a)
print(b)
print()
a, b, *c, d = (1, 2, 3, 4, 5, 6, 7)
print(a) #prints 1
print(b) #prints 2
print(c) #prints [3, 4, 5, 6]
print(d) #prints 1,2,7

print()

#Trick number 8
""" username = input('Username: ')
password = input('Password: ')

print('Logging In...') """

from getpass import getpass
username = input('Username: ')
password = getpass('Password: ')
print('Logging In...') 