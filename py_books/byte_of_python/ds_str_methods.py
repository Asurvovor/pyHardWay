name = 'Swaroop'
if name.startswith('Swa'):
    print('Yes, the string is starts with "Swa"')

if 'a' in name:
    print('Yes, it contais the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
