import requests
from bs4 import BeautifulSoup

URL = "https://www.geeksforgeeks.org/python-programming-language-tutorial/"
r = requests.get(URL)

soup = BeautifulSoup(r.text, 'html.parser')

headings = soup.find_all('h2')
for heading in headings:
    print(heading.text.strip())
