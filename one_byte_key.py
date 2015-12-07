import sys

cypher = sys.argv[1].decode('hex')

bestLetters = ['e', 'a', 't', 'n', 'o', 'h', 'i']
worstLetters = ['j', 'z', 'x', 'q', 'b']
bestMessage = ""
bestScore = -10000000
for i in range(0,255): 
  message = ""
  score = 0
  for j in range(0,len(cypher)):
    tmp = ord(cypher[j]) ^ i
    if chr(tmp) in bestLetters: 
      score += 3
    elif chr(tmp) in worstLetters: 
      score -= 1
    elif tmp < 0x20 or tmp > 0x128:
      score -= 50
    else: 
      score += 1
    message += chr(tmp)
  if score > bestScore: 
    bestMessage = message
    bestScore = score

if bestScore > 10: 
  print bestMessage

    

