#import request libs
import requests
from bs4 import BeautifulSoup

#URL of the page  to scrap
url = "https://example.com/"

response = requests.get(url)

#print the scrap data
if response.status_code==200:
    html_doc=response.content
    soup = BeautifulSoup(html_doc,'html.parser')

    tags = soup.find_all(['h1','p'])
    for tag in tags:
        print(tag.text.strip())
else:
    print("error")