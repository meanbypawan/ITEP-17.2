try:
 with open("file-collection/abc.txt") as f:
    for line in f:
      print(line)
 
except OSError as e:
  print(e) 