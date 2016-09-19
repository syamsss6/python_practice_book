# Write a program to list all files in the given directory.

import os
def list_files(x):
 p=os.path.abspath(x)
 for i in os.listdir(p):
  if i.endswith('.py') or i.endswith('txt'): 
    ss=os.stat(i)
    print "Name:\t",i,"\tLast Modification:\t",ss[-1],"\tSize\t",ss[-4]

list_files('.')
