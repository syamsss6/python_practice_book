def extsort(x):
 #p=x
 #print x.split('.')
 for i in x:
  p=i.split('.')
  print p[-1]
  
 
 
extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])

