import os

def print_count(path,extension):
  list_dir = []
  list_dir = os.listdir(path)
  count = 0
  for file in list_dir:
    if file.endswith(extension): 
      count += 1
  return count


count = print_count('/home/syam/python_practice_book_exercise/chap2','.py')
print count

