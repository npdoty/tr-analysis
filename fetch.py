import urllib2
import urllib
import re
import os
from pprint import pprint as pp
import csv
from bs4 import BeautifulSoup
import json

from gather import * 

STARTING_URL = "http://www.w3.org/TR/"

pp("Getting starting page %s" % STARTING_URL)

response = urllib2.urlopen(STARTING_URL)
html = response.read()
soup = BeautifulSoup(html)

rows = soup.select('div.data tr')
links = soup.select('td.table_titlecol > a')

# for link in links:
#   href = link.get('href')
#   short_name = href.split('/')[-1]
#   directory = archive_directory(short_name)
#   
#   # collect_html(directory, short_name, href)

entries = list()

for row in rows:
  entry = dict()
  link = row.select('td.table_datecol > a')[0]
  entry['date_published'] = unicode(link.string).encode("utf-8")
  title_link = row.select('td.table_titlecol > a')[0]
  entry['title'] = unicode(title_link.string).encode("utf-8")
  #pp(title_link.string)
  entry['href'] = title_link.get('href')
  entry['short_name'] = title_link.get('href').rstrip('/').split('/')[-1]
  status_link = row.select('td:nth-of-type(3) > a:nth-of-type(1)')[0]
  entry['document_status'] = unicode(status_link.string).encode('utf-8')
  entries.append(entry)

pp(len(entries))

entries = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in entries)]

pp(len(entries))

# for entry in entries:
#   directory = archive_directory(entry['short_name'])
#   collect_html(directory, entry['short_name'], entry['href'])

with open('tr.json', 'wb') as jsonfile:
  jsonfile.write(json.dumps(entries))

# with open('reports.csv', 'wb') as csvfile:
#   writer = csv.DictWriter(csvfile, ['short_name','title','date_published', 'href'])
#   writer.writerows(entries)