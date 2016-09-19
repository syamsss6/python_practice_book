import tablib
import re
def parse(fle):
 s=[]
 fl=open(fle)
 lines=fl.readlines()
 data = tablib.Dataset()
 for i in lines:
   p=re.findall('\w+',i)
   s.append(p)
 for i in range(len(s)):
  for j in range(0,3):
    data.append(s[i][j])

 with open("text.xls","wb") as f:
  f.write(data.xls)


parse('s.csv')
