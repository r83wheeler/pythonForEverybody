"""
Scraping Numbers from HTML using BeautifulSoup. In this assignment you will 
write a Python program similare to http:://www.py4e.com/code3/urllink2.py.
The program will use urllib to read the HTML from the data files below, and 
parse the data, extracting numbers and compute the sum of numbers in the file. 
We provide two files for this assignment. One is a simple file where we give
you the sum for your testing and the other is the actual data you need to process for the assignment. 

    Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum = 2553)
    Actual data:  http://py4e-data.dr-chuck.net/comments_1680935.html (Sum ends with 54)
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# parameter
content = []
total = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser

soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    content.append(tag.contents[0])

for i in range(len(content)):
    total = total + int(content[i])
print("Sum:", total)

