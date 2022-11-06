fruit = 'banana'

'n' in fruit

letter = fruit[1]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

print(len(fruit))

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

for letter in fruit:
    print(letter)

word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)

s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

print(s[:2])
print(s[8:])
print(s[:])
