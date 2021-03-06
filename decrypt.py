import string												# in order to get the set of required letters
from sys import argv										# we need argv to get the cmd parameters

x_letters = list(string.uppercase)							# turn the uppercase set of characters into a list
decrypt_keys = {}											# declare an empty dict
iter_length = len(x_letters) / 2							# store the half of the string length. for use later
for i in range(iter_length):								# loop from 0 to half of the string
	decrypt_keys[x_letters[i]] = x_letters[i+iter_length]	# the first half characters will be the keys to the last half characters
	decrypt_keys[x_letters[i+iter_length]] = x_letters[i]	# the last half characters will be the keys to the first half characters

if __name__ == '__main__':									# checks if this is the main script. proceed if true
	if len(argv)>1:											# checks if there are other arguments other than the filename
		for arg in argv[1:]:								# iterate from the 2nd argument til the last
			decrypted = ''									# declare an empty decrypted string
			encrypted = arg.upper()							# store the encrypted uppercase string
			for l in encrypted:								# iterate through the letters of the encrypted string
				decrypted += decrypt_keys[l]				# append the encrypted letter to the decrypted string
			print decrypted									# display the decrypted string