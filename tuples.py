d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)

tups = d.items()
print('first', tups) 

#############################
r = {'a':10, 'b':1, 'c':22}
r.items()

output = sorted(r.items())

print('second', output)
##############################

s = {'tiger':99, 'bryant':111, 'shasta':232}
t = sorted(s.items())
print('third', t)

for zen, wen in sorted(s.items()) :
    print(zen, wen)


c = {'p': 4, 'z':99, 'h': 22}
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )
    tmp.sort(reverse=True)

print(tmp)


days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

print(days[2])
