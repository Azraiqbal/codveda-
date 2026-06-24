filename = input("enter file name")
with open(filename,"r") as file:
    content = file.read()

encrypted_task = ""
shift = 3
for char in content:
    if char.islower():
        encrypted_task += chr(((ord(char) - 97 + shift) % 26) + 97)
    elif char.isupper():
        encrypted_task += chr(((ord(char) - 65 + shift) % 26) + 65)
    else:
        encrypted_task += char
print(encrypted_task)

with open("encrypted.txt","w") as file:
    file.write(encrypted_task)
decrypted_task = ""
for char in encrypted_task:
    if char.islower():
        decrypted_task += chr(((ord(char) - 97 - shift) % 26) + 97)
    elif char.isupper():
        decrypted_task += chr(((ord(char) - 65 - shift) % 26) + 65)
    else:
        decrypted_task += char
print(decrypted_task)

with open("decrypted.txt","w") as file:
    file.write(decrypted_task)

