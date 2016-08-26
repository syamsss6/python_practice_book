def group(list,size):
  i,j,k=1,1,0
  for s in list:
    l1=list[(size*k):(size)*j]
    print l1
    i,j,k=i+1,j+1,k+1


group([1,2,3,4,5,6,7,8,9,10],3)
