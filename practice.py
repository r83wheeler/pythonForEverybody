fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key, val)

x, y = 3, 4

print(x, y)

d = {'a':10, 'b':1, 'c':22}
path = d.items()

print(path)

quan = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
gx = quan.items()

print('gx', gx)



