""" The most commonly used object in the BeautifulSoup Library is, appropriately, the
 BeautifulSoup object."""

from urllib.request import urlopen
from bs4 import BeautifulSoup

# There are two main things that can go wrong in this line:
# -1. The page is not found on the server ( or an error in retrieving it). -"HTTPError"
# -2. The server is not found.
try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    # return null, break, or do some other "Plan B"
else:
    # program continues. Note: If you return or break in the
    # exception catch, you do not need to use the "else" statement
    bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
