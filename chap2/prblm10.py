
def unique(ls):
 op=[]
 for i in ls:
   if i not in op:
     op.append(i)

 print op



st=[]
limit=raw_input("enter limit")
for i in range(int(limit)):
 p=raw_input("enter val")
 st.append(int(p))
#print st

unique(st)
