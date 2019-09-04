#!/usr/bin/python3


# import hashlib to allow us to hash strings
import hashlib


# for colored terminal output
from termcolor import colored


# collect string from user
hash_value = input("[?] Please enter a string to hash: ")


# create hash object
hash_obj_1 = hashlib.md5()

# hash user's string
hash_obj_1.update(hash_value.encode())

# print hashed string
print(colored("MD5: " + hash_obj_1.hexdigest(), "cyan"))


hash_obj_2 = hashlib.sha1()
hash_obj_2.update(hash_value.encode())
print(colored("SHA1: " + hash_obj_2.hexdigest(), "magenta"))

hash_obj_3 = hashlib.sha224()
hash_obj_3.update(hash_value.encode())
print(colored("SHA224: " + hash_obj_3.hexdigest(), "yellow"))

hash_obj_4 = hashlib.sha256()
hash_obj_4.update(hash_value.encode())
print(colored("SHA256: " + hash_obj_4.hexdigest(), "green"))

hash_obj_5 = hashlib.sha512()
hash_obj_5.update(hash_value.encode())
print(colored("SHA512: " + hash_obj_5.hexdigest(), "blue"))


