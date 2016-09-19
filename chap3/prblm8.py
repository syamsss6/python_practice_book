import urllib
import re
def lnk(url):
 
 response=urllib.urlopen(url)
 p=response.read()
 links= re.findall('"((http)s?://.*?)"',p)
 #print links
 for i in links:
  print i

ip=raw_input("Enter the URL:  ")
lnk(ip)
