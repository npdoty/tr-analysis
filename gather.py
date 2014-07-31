import urllib
import re
import os
from pprint import pprint as pp

ARCHIVE_DIR = "archives"

def archive_directory(list_name):
  arc_dir = os.path.join(ARCHIVE_DIR,list_name)
  if not os.path.exists(arc_dir):
      os.makedirs(arc_dir)
  return arc_dir

def collect_html(directory, short_name, url):
  path = os.path.join(directory, short_name + '.html')
  if not os.path.isfile(path):
    pp("No cached entry. Saving to %s." % path)
    info = urllib.urlretrieve(url, path)
  else:
    pp("Already cached entry at %s." % path)