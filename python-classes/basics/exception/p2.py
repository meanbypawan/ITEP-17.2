'''
  sys.exit(0) # raise SystemExit Error
  os._exit(0)
'''
import os

print("At the start...")
try:
  os._exit(0)
except SystemExit:
    print("SystemExit Caught.....")
print("At the end...")