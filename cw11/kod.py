import hashlib


with open("obrazekkolor.bmp", "rb") as f:
    img1 = bytearray(f.read())

print("SHA-256:")
print(hashlib.sha256(img1).hexdigest())

print("bajty:", len(img1))

print("MD5:")
print(hashlib.md5(img1).hexdigest())


# zmiana jednego bity w setnym
img1[99] ^= 0b00000001


with open("obrazek_zmieniony.bmp", "wb") as f:
    f.write(img1)

print("SHA-256:")
print(hashlib.sha256(img1).hexdigest())

print("bajty:", len(img1))

print("MD5:")
print(hashlib.md5(img1).hexdigest())
