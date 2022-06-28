import geocoder
import os
os.system("Title Errordata#1337")
os.system('cls')
from slowprint.slowprint import slowprint
enter = input("Enter ip: ")
if enter == "":
    slowprint("IP cannot be empty!")
ip = geocoder.ip(f'{enter}')
print(ip.city)
print(ip.address)
print(ip.latlng)