import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#print(url)
d_json = urllib.request.urlopen(url, context=ctx).read()
decoded_json = d_json.decode()
info = json.loads(decoded_json)
lst = info["comments"]
#for item in info:
#    print(item["note"])
sum = 0
for item in lst:
    #print(item['count'])
    sum =  sum + int(item['count'])
print(sum)
