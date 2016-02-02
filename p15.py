

def checkPadding(message):
  lastByte = message[-1]
  for i in range(1,ord(lastByte)+1):
    if message[-i] != lastByte:
      return False
  return True


print "True = " + str(checkPadding("ICE ICE BABY\x04\x04\x04\x04"))
print "False = " + str(checkPadding("ICE ICE BABY\x05\x05\x05\x05"))
print "False = " + str(checkPadding("ICE ICE BABY\x01\x02\x03\x04"))
