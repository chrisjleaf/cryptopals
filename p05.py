from tools.utils import cipher_enc

text = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"

print cipher_enc(text, "ICE").encode('hex')
