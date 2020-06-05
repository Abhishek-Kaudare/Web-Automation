import requests
from bs4 import BeautifulSoup
import csv
import re
import sys

site_url = 'https://www.trustedchoice.com'
page = requests.get(site_url+'/agent')

soup = BeautifulSoup(page.content, 'html.parser')
divs = soup.find_all("div", class_="col-xs-12 col-sm-3")

with open('agents.csv', 'w', newline='') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 1
  write = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  write.writerow(['Sr. No','Name','State','City','Zip-Code','Phone','Category','Site'])
  for div in divs:
    print(site_url+str(div.a['href']))
    page_a = requests.get(site_url+str(div.a['href']))
    soup_a = BeautifulSoup(page_a.content, 'html.parser')
    state = soup_a.select_one("div.breadcrumbs span:nth-of-type(3)").text.strip()
    divs_a = soup_a.find_all("div", class_="col-xs-12 col-sm-3")
    # print(divs_a)
    
    # break
      
    for div_a in divs_a:
      page_b = requests.get(site_url+str(div_a.a['href']))
      soup_b = BeautifulSoup(page_b.content, 'html.parser')
      city = soup_b.select_one("div.breadcrumbs span:nth-of-type(4)").text.strip()
      print(state)
      print(city)
      addrs = soup_b.find_all("address", class_="col-xs-12 col-sm-4")
      for add in addrs:
        zip_r = add.div.div.text.splitlines()[-3]

        # value fields
        site_a = site_url+str(add.div.div.a['href']).strip()
        name = add.div.div.a.text.strip()
        zip_p = ''.join(c for c in zip_r if c in '0123456789-_+')
        phone = add.div.div.text.splitlines()[-2].strip()
        cat = add.div.div.text.splitlines()[-1].strip()
        print(site_a)
        print(name)    
        print(zip_r,zip_p)
        print(phone)
        print(cat)
        # print(re.findall(r'[0-9]+', add.div.div.text.splitlines()[-3]))


        write.writerow([line_count,name,state,city,zip_p,phone,cat,site_a])
        line_count = line_count + 1
        if line_count == 50:
          sys.exit()
      # break

      # print(str(div.a['href']))
    # break
