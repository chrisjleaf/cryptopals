import struct

def pkcs_pad_block(text,block_length=16):
  pad_length = block_length - ( len(text) % block_length )
  if pad_length == 0:
    pad_length = block_length

  return text + chr(pad_length)*pad_length
