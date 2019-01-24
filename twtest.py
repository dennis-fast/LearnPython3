import urllib.request, urllib.parse, urllib.error
from twurl import augment
import json
import ssl
import pprint

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

print('* Calling Twitter...')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
              {'screen_name': 'drchuck', 'count': '2'})
print(url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()
js_data = json.loads(data)
print(json.dumps(js_data, indent=4))

profile_name = js_data[0]['user']['name']
followers = js_data[0]['user']['followers_count']
print('profile_name', profile_name, 'followers', followers)

# print ('======================================')
# headers = dict(connection.getheaders())
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(headers)
