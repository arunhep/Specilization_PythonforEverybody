# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
        # Look at the parts of a tag
    sum = sum + int(tag.contents[0])
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    #print(tag.get('href', None))
print(sum)
'''
