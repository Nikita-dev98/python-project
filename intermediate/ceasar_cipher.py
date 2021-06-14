#!bin/bash/python

alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

class CeasarCipher:
	def _init_(self,text,shift):
		self.text = text
		self.shift = shift
def encode(self,str,shift):
		encode = ''
		str = str.lower()
		for i in str:
			if i in alphabet:
				encode += alphabet[alphabet.index(i) + shift]
			else:
				encode+=i
		return encode.upper()

def decode(self,str,shift):
		decode=''
		str = str.lower()
		for i in str:
			if i in alphabet:
				decode += alphabet[alphabet.index(i) - shift]
			else:
				decode+=i
		return decode.upper()


obj1 = CeasarCipher("john",2)
print(obj1.encode("max",3))

