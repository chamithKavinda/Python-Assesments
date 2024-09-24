import requests
import xlsxwriter
from bs4 import BeautifulSoup

# initialize xlsxwriter
workbook = xlsxwriter.Workbook('scrapped_vehical_data.xlsx')
worksheet = workbook.add_worksheet()

# write headers
headers = ['Name', 'Year', 'Price', 'From', 'Model Year']
for col_num, header in enumerate(headers):
    worksheet.write(0, col_num, header)

row = 1
for page_num in range(1, 6): 
    url = f"https://www.patpat.lk/vehicle?page={page_num}"
    response = requests.get(url)

    if response.status_code == 200:
        html_doc = response.content
        html_doc = BeautifulSoup(html_doc, 'html.parser')
        elements = html_doc.find_all('div', class_='result-item result-item-vehicle result-item-promoted col-10 col-sm-6 col-md-5 col-lg-12 mb-3')

        for element in elements:
            name = element.find('h4', class_='result-title').text.strip()
            year = element.find('span', class_='mobile-only').text.strip()
            price = element.find('label', class_='w-100').text.strip()
            from_loc = element.find_all('span', class_='d-block w-auto float-left')[0].text.strip()
            model_year = element.find_all('span', class_='d-block w-auto float-left')[1].text.strip()
            data = [name, year, price, from_loc, model_year]
            for col_num, cell_data in enumerate(data):
                worksheet.write(row, col_num, cell_data)
            row += 1

# Close the workbook
workbook.close()