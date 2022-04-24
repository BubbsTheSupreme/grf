from os import urandom
from sys import argv

KB = 1024
MB = 1048576
GB = 1073741824

count = int(argv[2])

if argv[3].lower() == 'kb': total = count * KB
elif argv[3].lower() == 'mb': total = count * MB
elif argv[3].lower() == 'gb': total = count * GB

with open(argv[1], 'wb') as f:
	f.write(urandom(total))