def unique(ls):
 op=[]
 for i in ls:
   if i not in op:
     op.append(i)
 print "unique list is:",op


st=(1,2,5,1,3,2,1,3,2,4)
unique(st)



