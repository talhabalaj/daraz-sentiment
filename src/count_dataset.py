from glob import glob
import json
from configuration import *

count = 0
for each in glob(f'{data_dir}/*.json'):
  with open(each) as f:
    count += len(json.loads(f.read()))

print(count, end='\r')
