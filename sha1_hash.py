#!/usr/bin/python3

# import fg from colored for color terminal
from colored import fg

# import urlopen to allow us to open urls
from urllib.request import urlopen

# import hashlib to hash strings
import hashlib


# collect sha1 hash from user
sha1_hash = input("[?] Please enter a SHA1 hash: ")

# read password list from github raw url
pass_list = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

# for each password in password list
for password in pass_list.split("\n"):

    # hashes password in sha1
    hash_guess = hashlib.sha1(bytes(password, "utf-8")).hexdigest()
    
    # if hashed password equals hash collected from user
    if hash_guess == sha1_hash:
        print("%s[+] The password is: {}".format(str(password)) % (fg(46)))
        quit()
    else:
        print("%s[-] The password is not: {}".format(str(password)) % (fg(203)))

print("[-] The password is not in the password list" % (fg(203)))
