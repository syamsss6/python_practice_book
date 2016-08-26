#def reverse(list):
# for i in list:
#   print list[-i]
#reverse([1,2,3])

def reverse(list):
 p=[ ]
# n=len(list)
 cnt=1
 for i in range(0,len(list)):
  p.append(list[len(list)-cnt])
  cnt+=1
 print p

reverse([1,2,3,4])
reverse(reverse([5,6,7,8]))
 
