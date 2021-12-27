import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.december.com/html/spec/colorshades.html'
page  = requests.get(url)
# print(page.text)
soup = BeautifulSoup(page.content, "html.parser")

# divs = soup.find_all('table',{'class':"c"})

th_results = soup.find_all('tr')
# 
print(len(th_results))
# 
color_list = []
# ------- # ------- #
for i in th_results:
    temp_list = []
    for th in i:
        temp_list.append(th.text)
    color_list.append(temp_list)

for i in color_list:
    for j in i:
        if j == '\xa0':
            i.remove(j)
  
# field names 
fields = color_list[0] 
    
# data rows of csv file 
rows = color_list[1:] 
  
with open('out.csv', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(rows)    

print(color_list[0])