def dump(x):
 op=[]
 for i in x:
  if x not in op:
   op.append(x)
 return op   
 #for i in x:
 #  if i==x:
 #print op
op=dump([1,2,1,3,2,5])
print op

