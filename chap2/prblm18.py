def reverse(file):
 f=open(file)
 p=f.readlines()
 p.reverse()
 for i in p:
   print i




reverse('she.txt')
