import json
import urllib.request

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2423575.json'
    
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved',len(data),'characters')

info = json.loads(data)
print('User count:', len(info['comments']))

total = 0
for item in info['comments']:
    total = total + int(item['count'])
print(total)