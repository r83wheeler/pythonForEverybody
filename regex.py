#search for lines that start with 'X' followed by any 
#non whitesplace characters and ':' followed by a space
#and any number. The number can include a decimal. 
#Then print the number if it is greater than zero.

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)



test = 'From: Using the : character'
toast = re.findall('^F.+:', test)
print(toast)

example = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

answer = re.findall('\S+?@\S+', example)
print(answer)

