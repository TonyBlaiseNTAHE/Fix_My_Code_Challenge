#!/usr/bin/python3
import hashlib


password = "Tony"
result = hashlib.md5(password.encode()).hexdigest()
print(result)