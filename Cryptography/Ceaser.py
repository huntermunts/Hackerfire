ciphertext = "uapv{ndj'kt_qtvjc_ndjg_rgneid_psktcijgth}"


def shift(text, shift):
	s = ''
	for i in text:
		o = chr(((ord(i)-96+shift)%26+96))
		s+=o
	print(s)


for x in range(26):
	shift(ciphertext, x)
