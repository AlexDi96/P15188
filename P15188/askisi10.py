import urllib
from bs4 import BeautifulSoup

# Declare global variables
href_list = []
p_list = []
br_list = []
no_iterations = 0

# Prompt user for input
url = raw_input('Enter url - ')


# Scraping the url
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    href_list.append(tag.get('href', None))

# Retrieve all of the p tags
p = soup('p')
for p in p:
    p_list.append(p.get('p', None))


# Retrieve all of the br tags
br = soup('br')
for br in br:
    br_list.append(br.get('br', None))

# Printing info for user
print "Total hyperlinks tags: ",len(href_list)
print "Total line changes: ",len(p_list + br_list)
