import urllib2
import urllib
import re
import os
from pprint import pprint as pp
import csv
from bs4 import BeautifulSoup
import json
from gather import * 

JSON_INPUT_FILENAME = 'tr.json'
JSON_OUTPUT_FILENAME = 'tr-search.json'

search_terms = ['privacy','security','Web']

def file_for_shortname(shortname):
  path = os.path.join(ARCHIVE_DIR, shortname, shortname + '.html')
  if os.path.isfile(path):
    return path
  
  return None

with open(JSON_INPUT_FILENAME, 'r') as jsonfile:
  entries = json.load(jsonfile)
  
  for entry in entries:
    tr_file = file_for_shortname(entry['short_name'])
    with open(tr_file, 'r') as html_file:
      html = html_file.read()
      soup = BeautifulSoup(html)
      text = soup.get_text()
      
      for term in search_terms:
        matches = re.findall(term, text, flags=re.IGNORECASE)
        entry[term+'_search'] = len(matches)
        pp("Found %d instances of %s" % (entry[term+'_search'], term))
  
  with open(JSON_OUTPUT_FILENAME, 'wb') as outfile:
    outfile.write(json.dumps(entries))
