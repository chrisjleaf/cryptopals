from collections import defaultdict
import re
with open('pg84.txt','r') as f:
  text = " ".join(f.readlines())
with open('pg74.txt','r') as f:
  text += " ".join(f.readlines())
with open('pg98.txt','r') as f:
  text += " ".join(f.readlines())
with open('pg844.txt','r') as f:
  text += " ".join(f.readlines())
with open('pg1400.txt','r') as f:
  text += " ".join(f.readlines())
with open('pg5200.txt','r') as f:
  text += " ".join(f.readlines())
with open('pg4300.txt','r') as f:
  text += " ".join(f.readlines())
with open('pg30254.txt','r') as f:
  text += " ".join(f.readlines())

freqs = defaultdict(float)

count = 0
for c in re.findall('[A-Za-z ,.!()]', text):
  freqs[c.lower()] += 1
  count += 1
 
for k,c in freqs.items():
  print "'" + str(k) + "'" + ":" + str(c/count) + ","
