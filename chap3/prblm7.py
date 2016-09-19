import re
def make_slug(name):
 lst=re.findall('\w+',name)
 lst1='-'.join(lst)
 print lst1

make_slug("hello world")
make_slug("hello  world!")
make_slug(" --hello-  world--")
