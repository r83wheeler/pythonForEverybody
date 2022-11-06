fruit = 'banana'
word = 'banana'
'n' in fruit

if 'a' in fruit :
    print('Found it!')

if word == 'banana' :
    print('All right, bananas.')

if word < 'banana' :
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana' :
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')


greet = 'Hello Bob'
zap = greet.lower()
print(zap)

print(greet)

nstr = greet.replace('Bob', 'Jane')
print(nstr)

print('Hi There' .lower())

stuff = 'Hello world'
type(stuff)

directory = dir(stuff)
print(directory)

r = str.capitalize('russ')
print(r)

pos = fruit.find('na')
print(pos)

aa = fruit.find('z')
print(aa)
