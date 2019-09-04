#!/usr/bin/python3

# import crypt library to allow hash salting
import crypt

# import fg from colored for color terminal output
from colored import fg


# accepts hashed and salted password to compare to salted word
def crack_pass(crypt_word):
    # capture hash salt
    salt = crypt_word[0:2]

    # open dictionary file for reading
    dictionary = open('dictionary.txt','r')
    
    # for each line in dictionary.txt
    for word in dictionary.readlines():

        # strip the newline character
        word = word.strip('\n')

        # salt password hash
        crypt_pass = crypt.crypt(word, salt)

        # if salted password hash equals salted word hash
        if crypt_word == crypt_pass:

            # print password found
            print("%s[+] Password found: {}".format(word) % (fg(82)))
            
            # exit program
            quit()

    print("%s[-] Password not found." % (fg(166)))


def main():
    # opens password file for reading
    pass_file = open('crypt_pass.txt', 'r')

    # for each line in password file
    for line in pass_file.readlines():

        # if the line contains a colon
        if ":" in line:

            # split line at colon and select first item in list
            user = line.split(':')[0]

            # split line at colon, select second item, and strip newline
            crypt_word = line.split(':')[1].strip('\n')

            # print current password being cracked
            print("%s[*] Cracking password for: {}".format(user) % (fg(75)))
            
            # pass hashed and salted word to crack_pass
            crack_pass(crypt_word)


main()
