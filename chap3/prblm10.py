import urllib
import json

def myip():
    data = json.loads(urllib.urlopen("http://httpbin.org/get").read())
    print data['origin']

myip()





