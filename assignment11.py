#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers. 


import re 
count = 0
hand = open("regex_sum_1680933.txt")
lines = hand.read()
match = re.findall('[0-9]+', lines)
for i in match:
    number = int(i)
    count = count + number
print(count)