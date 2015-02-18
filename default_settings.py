import string												# in order to get the set of required letters

x_letters = list(string.uppercase)							# turn the uppercase set of characters into a list
decrypt_keys = {}											# declare an empty dict
iter_length = len(x_letters) / 2							# store the half of the string length. for use later
for i in range(iter_length):								# loop from 0 to half of the string
	decrypt_keys[x_letters[i]] = x_letters[i+iter_length]	# the first half characters will be the keys to the last half characters
	decrypt_keys[x_letters[i+iter_length]] = x_letters[i]	# the last half characters will be the keys to the first half characters