def enumerates(n):
 indx=[]
 p=n
 for i in p:
   indx.append(p.index(i))
 
 print zip(indx,p)

enumerates(["a","b","c"])
