def cumulative_product(lst):
 op=[ ]
 pro=1
 for i in lst:
  pro*=i
  op.append(pro)
 print op
cumulative_product([1,2,3,4])

cumulative_product([4,3,2,1])
