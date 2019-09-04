#!/usr/bin/python3


# import fg from colored for color terminal output
from colored import fg

# import hashlib to hash strings
import hashlib


# trues to open a file for reading
def try_open(wordlist):
    try:
        pass_file = open(wordlist, "r")
        return pass_file
    except:
        print("[?] Unable to locate password file.")


# collect hash and password file from user
pass_hash = input("[?] Enter an MD5 hash value: ")
wordlist = input("[?] Enter path to the password file: ")

# opens password file for reading
pass_file = try_open(wordlist)


# for each word in the password file
for word in pass_file:
    print("%s[*] Trying {}".format(word.strip('\n')) % (fg(45)))
    
    # encode the word in utf-8
    encoded_word = word.encode('utf-8')

    # create md5 hash
    md5_digest = hashlib.md5(encoded_word.strip()).hexdigest()
    
    # if md5 hash equals password hash collected from user
    if md5_digest == pass_hash:
        print("%s[+] Password found: {}".format(word.strip('\n')) % (fg(40)))
        quit()


print("%s[-] Password not in list." % (fg(196)))
