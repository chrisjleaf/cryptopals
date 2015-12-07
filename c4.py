import sys
import re
text = ""
with open(sys.argv[1],'r') as f: 
  lines = f.readlines()
  for line in lines: 
    text += line.rstrip().decode('hex')

bestLetters = ['e', 't', 'a', 'o']
goodLetters = ['i', 'n', 's', 'h']
badLetters = ['k', 'v', 'b']
worstLetters = ['j', 'q', 'x', 'z']
for t in range(0,len(text),30):
  line = text[t:t+30]
  bestMessage = ""
  bestScore = -10000000
  for i in range(0,255): 
    message = ""
    score = 0
    for j in range(0,len(line)):
      tmp = ord(line[j]) ^ i
      if chr(tmp) in bestLetters: 
        score += 3
      elif chr(tmp) in goodLetters: 
        score += 1
      elif chr(tmp) in badLetters: 
        score -= 1
      elif chr(tmp) in worstLetters: 
        score -= 3
      elif re.match('[^a-zA-Z ]',chr(tmp)):
        score -= 5
      message += chr(tmp)
    if score > bestScore: 
      bestMessage = message
      bestScore = score
  print bestMessage


    
