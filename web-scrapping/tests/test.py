import requests
import re
from bs4 import BeautifulSoup

request = requests.get(r'http://www.zoover.es/espana/tenerife/playa-de-las-americas/h10-conquistador/hotel')

html = request.content

print(html)
soup = BeautifulSoup(html, 'html.parser')
matches = soup.findAll("div", class_=r'contribution-item-content')
print(matches)
for match in matches:
    print(match)
