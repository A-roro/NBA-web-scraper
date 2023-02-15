import requests
import csv
from bs4 import BeautifulSoup

# Scrape the NBA data from the website
url = 'https://www.nba.com/stats/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
data = []

# Find the NBA data and extract it
table = soup.find('div', {'class': 'stats-table-view'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

# Save the data to a CSV file
with open('nba_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player', 'Team', 'Points'])
    for row in data:
        writer.writerow(row)
