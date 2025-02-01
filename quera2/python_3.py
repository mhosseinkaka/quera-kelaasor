import string
n = int(input())
m = str(input())
x = ""

for char in m:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        new_char = chr(start + ((ord(char) - start + n) % 26))
        x += new_char
    else:
        x += char

print(x)
