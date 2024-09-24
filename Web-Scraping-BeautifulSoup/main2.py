#import request libs
import requests
import xlsxwriter
from bs4 import BeautifulSoup
from PIL import Image

#url of the page to scrap
url = "https://www.geeksforgeeks.org/fundamentals-of-algorithms/"
response = requests.get(url)

#xls write config
workbook = xlsxwriter.Workbook('scrapped_data.xlsx')
worksheet = workbook.add_worksheet()

#save the scrap data
if response.status_code==200:
    html_doc=response.content
    soup = BeautifulSoup(html_doc,'html.parser')
    row = 0
    h2_tags = soup.find_all('h2')
    for h2 in h2_tags:
        worksheet.write(row, 0, h2.text.strip())
        ul = h2.find_next('ul')
        if ul:
            li_tags = ul.find_all('li')
            for i in range(len(li_tags)):
                worksheet.write(row + i, 1, li_tags[i].text.strip())
            if len(li_tags) > 0:
                row =row + len(li_tags)
            else:
                row =row + 1
        else:
            row = row + 1
        row = row + 1

    # alt="What is Algorithm?"
    image = soup.find('img', alt="What is Algorithm?")
    image_url = image['src']
    print(image_url)
    img = Image.open(requests.get(image_url, stream = True).raw)
    img.save('image.jpg')
    
    workbook.close()
else:
    print("error")