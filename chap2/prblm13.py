
def lensort(a):
 a.sort(key=lambda x:len(x))
 print a
lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
