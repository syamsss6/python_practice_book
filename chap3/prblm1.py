# Write a program to list all files in the given directory.

import os
def list_files(x):
 p=os.path.abspath(x)
 for i in os.listdir(p):
 #print p
 #for i in p: 
  if i.endswith('.py') or i.endswith('txt'): 
    print i

list_files('.')
