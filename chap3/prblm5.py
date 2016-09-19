def wget(url):

    import urllib
    import os
    basename=os.path.basename(url)
    if basename == '':
        fle=open("index.html","w")
        response = urllib.urlopen(url)
        p=response.read()
        fle.write(p)
    else:
        fle=open(basename,"w")
        response = urllib.urlopen(url)
        p=response.read()
        fle.write(p)
    fle.close()


ip=raw_input('Enter url: ')
wget(ip)





