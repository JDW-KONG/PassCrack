#!/usr/bin/python3


import crypt
from colored import fg


def crack_pass(crypt_word):
    salt = crypt_word[0:2]
    dictionary = open('dictionary.txt','r')
    for word in dictionary.readlines():
        word = word.strip('\n')
        crypt_pass = crypt.crypt(word, salt)
        if crypt_word == crypt_pass:
            print("%s[+] Password found: {}".format(word) % (fg(82)))
            quit()

    print("%s[-] Password not found." % (fg(166)))


def main():
    pass_file = open('crypt_pass.txt', 'r')
    for line in pass_file.readlines():
        if ":" in line:
            user = line.split(':')[0]
            crypt_word = line.split(':')[1].strip('\n')
            print("%s[*] Cracking password for: {}".format(user) % (fg(75)))
            crack_pass(crypt_word)


main()
