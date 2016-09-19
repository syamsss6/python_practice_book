import os
import re
import urllib

def wget(url):

    basename=os.path.basename(url)
    if basename == '':
        fle=open("index.html","w")
        response = urllib.urlopen(url)
        p=response.read()
        fle.write(p)
    
        remove_html('index.html')	
    else:
        fle=open(basename,"w")
        response = urllib.urlopen(url)
        p=response.read()
        fle.write(p)
        remove_html(basename)
    fle.close()

def remove_html(filename):
    f=open(filename,'r')
    strings = re.findall(r'>[^<]+<', f.read())
    for i in strings:
        print i[1:-1]


ip=raw_input('Enter url: ')
wget(ip)

