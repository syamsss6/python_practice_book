def lines(file):
 with open(file,"r") as s:
  for lines in s:
    if len(lines) > 40:
      print lines


lines('b.txt')
