# We'll look at Parsing Complicated HTML Pages in order to extract only the information we need.
# Searching for tags by attributes, working with lists of tags, and parse tree navigation.
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
namelist = bsObj.findAll("span", {"class":"green"})
#Call .get_text() last, only before printing, storing or manipulating your final data. In, general, try to preserve the tag structure of a document as long as possible.
for name in namelist:
    print(name.get_text())
