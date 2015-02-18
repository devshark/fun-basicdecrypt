import string										# in order to get the set of required letters
from sys import argv								# we need argv to get the cmd parameters

x_letters = list(string.uppercase)					# turn the uppercase set of characters into a list
decrypt_keys = {}									# declare an empty dict
for i in range(13):									# loop from 0 to 12
	decrypt_keys[x_letters[i]] = x_letters[i+13]	# the first 13 characters will be the keys to the last 13 characters
	decrypt_keys[x_letters[i+13]] = x_letters[i]	# the last 13 characters will be the keys to the first 13 characters

if __name__ == '__main__':							# checks if this is the main script. proceed if true
	if len(argv)>1:									# checks if there are other arguments other than the filename
		for arg in argv[1:]:						# iterate from the 2nd argument til the last
			decrypted = ''							# declare an empty decrypted string
			encrypted = arg.upper()					# store the encrypted uppercase string
			for l in encrypted:						# iterate through the letters of the encrypted string
				decrypted += decrypt_keys[l]		# append the encrypted letter to the decrypted string
			print decrypted							# display the decrypted string