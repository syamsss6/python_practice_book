import re
def parse(fl):
 s=[]
 fle=open(fl)
 p=fle.readlines()
 for i in p:
  if not  i.startswith("#"):
   tmp=re.findall('\w+',i)
   s.append(tmp)
 print s
  
    

parse('a.txt')
