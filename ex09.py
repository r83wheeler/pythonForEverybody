fname = input("Enter File: ")
if len(fname) < 1: fname = 'clown.txt'
handle = open(fname)

di = dict()
for lin in handle:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        # idiom: retrieve/create/update counter  
        di[w] = di.get(w,0) + 1
        #print(w,'new',di[w])

#print(di)

#now we want to find the most common word
largest = -1
theWord = None 
for k,v in di.items() :
    print(k,v)
    if v > largest :
        largest = v 
        theWord = k #capture/remember the largest key

print('Done', theWord, largest)
