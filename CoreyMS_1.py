#source https://www.youtube.com/watch?v=C-gEQdGVXbk

print()
#Python trick #7#   
class Person:
    pass

person=Person()

""" person.first = 'Samir'
person.last = 'Aghayev'

print(person.first, person.last) """

first_key ='first'
first_val = 'Samir'

person.first=""

setattr(person, 'first', 'Samir')
setattr(person, first_key, first_val) #the same effecta as above but we can use variable names


print(person.first)
first = getattr(person,first_key)
print(first)

person_info = { 'first': 'Samir', 'last':'Aghayev'}
for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))
