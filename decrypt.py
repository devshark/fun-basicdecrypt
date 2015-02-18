from sys import argv										# we need argv to get the cmd parameters
from utils import decrypt_string							# import the required function from utils file

if __name__ == '__main__':									# checks if this is the main script. proceed if true
	if len(argv)>1:											# checks if there are other arguments other than the filename
		for arg in argv[1:]:								# iterate from the 2nd argument til the last
			print decrypt_string(arg)						# print the decrypted string returned from function
