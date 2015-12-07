from Crypto.Cipher import AES
from strxor import strxor
from pkcs7 import pkcs_pad_block as pad_message

def CBC_decrypt(cipher, text, IV):
  previous = IV
  blockLen = 16
  plain = ""
  for i in range(0,len(text),blockLen):
    block = text[i:i+blockLen]
    t = cipher.decrypt(block)
    plain += strxor(t,previous)
    previous = block
  padLen = ord(plain[-1])
  return plain[:-padLen]


def CBC_encrypt(cipher, text, IV):
  previous = IV
  blockLen = 16
  cipher_text = ""
  text = pad_message(text, blockLen)

  for i in range(0,len(text),blockLen):
    t = strxor(text[i:i+16], previous)
    block = cipher.encrypt(t)
    cipher_text += block
    previous = block

  return cipher_text
