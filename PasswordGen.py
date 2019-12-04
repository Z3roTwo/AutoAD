import random, string

chars = "abcdefghijklmnopqrstuvwxyz"
chars1 = "1234567890"
chars2 = "!#%&/()="
password = ""
for c in range(2):
    password += random.choice(chars)
    password += random.choice(chars.upper())
    password += random.choice(chars1)
    password += random.choice(chars2)
password = ''.join(random.sample(password, len(password)))
print(password)
print(len(password))

print("asdasd", "asdasd")