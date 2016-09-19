import os
from os.path import join, splitext
from glob import  glob
from collections import Counter
def extcount(x):
 path=os.path.abspath(x)
 c = Counter([splitext(i)[1][1:] for i in glob(join(path, '*'))])
 for ext, count in c.most_common():
    print ext, count

extcount('/home/syam/')
