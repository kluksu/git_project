import getopt
import re
from termcolor import colored
import sys
password=""
if(len(sys.argv)>1):
    password=sys.argv[1]
# regex = "^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])[A-Za-z\d]{10,}$"
regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{10,}$"
speciel="^(?=.*[!@#$%^&*])"
capital="^(?=.*[A-Z])"
lowerCase="^(?=.*[a-z])"
number="^(?=.*\d)"
if re.fullmatch(regex,password):
    print(colored(True, 'green'))
    exit(0)

else:
    print(colored(False, 'red'))
    if(re.match(speciel,password)):
        print(colored('no special characters are allowd', "red"))
    if(len(password)<10):
        print(colored("password must be at least 10 characters long", "red"))
    if not (re.match(capital, password)):
        print(colored('your password must include one capital letter at least', "red"))
    if not (re.match(lowerCase, password)):
        print(colored('your password must include one lower Case letter at least', "red"))
    if not (re.match(number, password)):
        print(colored('your password must include one digit at least', "red"))

    exit(1)





