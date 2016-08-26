#implement unix command grep

def grep(fle,string):
 with open(fle) as f:
  lines = f.readlines()
 for line in lines:
  if string in line:
   print line

grep('she.txt','sure')
