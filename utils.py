from settings import decrypt_keys							# need to import the decrypt_keys for decryption

def decrypt_string(encrypted_string):						# create function for reuse.
	decrypted = ''											# declare an empty decrypted string
	encrypted = encrypted_string.upper()					# store the encrypted upper-case string
	for l in encrypted:										# iterate through the letters of the encrypted string
		decrypted += decrypt_keys[l]						# append the encrypted letter to the decrypted string
	return decrypted										# return the decrypted string