def center(fle,width):
 lines=open(fle).readlines()
 stripped=[]
 for line in lines:
   print(line.center(width))
center('she.txt',80)
