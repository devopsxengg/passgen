import string
import random
import sys

if sys.argv[1].isdigit():
    x = string.ascii_lowercase + string.ascii_uppercase + string.digits
    print("The random generated password is: \n")
    print(''.join(random.sample(x, int(sys.argv[1]))))
else:
    print("Invalid Entry")
