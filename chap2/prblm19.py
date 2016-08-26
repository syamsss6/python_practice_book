def head(fle,N):
 
 f=open(fle)
 
 print "------head-----------"
 for i in range(N):
  head=f.next()
  print head
 print "---------------------"

def tail(fle,N):
 s=[]
 print "--------tail----------"
 p=open(fle)
 for i in p:
  s.append(i)
 x=int(len(s)-N)
 y=int(len(s))
 print ''.join(s[x:y])
 print "-----------------------"
head('txt.txt',10)
tail('txt.txt',10)
