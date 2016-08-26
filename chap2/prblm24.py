def zip(a,b):
 if len(a)<len(b):
  return [(a[i],b[i]) for i in range(len(a))]
 else:
  return [(a[i],b[i]) for i in range(len(b))]
p=zip([2,3,4,5],['a','b','c','d'])
print p


