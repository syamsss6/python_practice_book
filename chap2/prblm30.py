#\w is a character class, which is a shortcut for [a-zA-Z0-9_] 

import re
def parse(fle):
 s=[]
 fl=open(fle)
 lines=fl.readlines()
 for i in lines:
   p=re.findall('\w+',i)
   s.append(p)
 print s
parse('s.csv')

