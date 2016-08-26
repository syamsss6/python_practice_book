def filter(f,a):
 return [x for x in a if f(x) is True]
def even(n):
 return n%2==0

print filter(even,range(10))
