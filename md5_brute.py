#!/usr/bin/python3

from colored import fg
import hashlib


def try_open(wordlist):
    try:
        pass_file = open(wordlist, "r")
        return pass_file
    except:
        print("[?] Unable to locate password file.")


pass_hash = input("[?] Enter an MD5 hash value: ")
wordlist = input("[?] Enter path to the password file: ")
pass_file = try_open(wordlist)


for word in pass_file:
    print("%s[*] Trying {}".format(word.strip('\n')) % (fg(45)))
    encoded_word = word.encode('utf-8')
    md5_digest = hashlib.md5(encoded_word.strip()).hexdigest()

    if md5_digest == pass_hash:
        print("%s[+] Password found: {}".format(word.strip('\n')) % (fg(40)))
        quit()


print("%s[-] Password not in list." % (fg(196)))
