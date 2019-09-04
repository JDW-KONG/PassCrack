#!/usr/bin/python3

from colored import fg
from urllib.request import urlopen
import hashlib



sha1_hash = input("[?] Please enter a SHA1 hash: ")

pass_list = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

for password in pass_list.split("\n"):
    hash_guess = hashlib.sha1(bytes(password, "utf-8")).hexdigest()
    if hash_guess == sha1_hash:
        print("%s[+] The password is: {}".format(str(password)) % (fg(46)))
        quit()
    else:
        print("%s[-] The password is not: {}".format(str(password)) % (fg(203)))

print("[-] The password is not in the password list" % (fg(203)))
