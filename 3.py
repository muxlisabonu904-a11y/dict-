
import os
os.system("cls")

login = {
    "jeymsbond" : "agent007",
    "tony_stark" : "ironman101",
    "piterparker": "spider12.12",
    "sherlok": "sher.104"
}

ism = input("Username kiriting:")
parol = input("Parol kiriting:")

if ism in login:
    if login[ism] == parol:
        print("hisobga kirdingiz")
    else:
        print("parol notogri")
else:
    print ("bunday foydalanuvchi yuq")
