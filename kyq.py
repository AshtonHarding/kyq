import urllib.request
from bs4 import BeautifulSoup
import sys

## Requirements
# pip3 install bs4 --user
## NOTE: This is a tempory solution for now.
##       I really need this to work via bash
##       or through the youtube API.
user_query = ""

for x in range(1, len(sys.argv)):
  user_query += sys.argv[x]
  user_query += " "

query = urllib.parse.quote(user_query)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    if ("/user/" not in vid['href']) and ("&list" not in vid['href']):
     vals = 30 - len(vid['href'])
     spaces = vals * ' '
     print(' https://www.youtube.com' + vid['href'] + spaces + vid['title'])

