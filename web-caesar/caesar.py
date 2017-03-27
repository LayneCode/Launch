

def alphabet_position(text):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	alphaU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	if text in alpha:
		return alpha.index(text)
	if text in alphaU:
		return alphaU.index(text)	
	

def rotate_character(text, rot):
	
	alpha = "abcdefghijklmnopqrstuvwxyz"
	alphaU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	oldchar = alphabet_position(text)
	newindex = (oldchar + rot) % 26
	
	if text in alpha:
		return alpha[newindex]
	if text in alphaU:
		return alphaU[newindex]

def encrypt(text, rot):

	alpha = "abcdefghijklmnopqrstuvwxyz"
	alphaU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	enc = ""

	for letter in text:
		if letter not in alpha and letter not in alphaU:
			enc += letter
		else:
			enc += rotate_character(letter, rot)

	return enc