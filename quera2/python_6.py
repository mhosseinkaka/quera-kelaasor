from collections import Counter

def creat(text):
    text = text.replace(" ","").lower()
    l = []
    char = Counter(text)
    for key, value in char.items():
        if value == 1:
            l.append(key)
    if len(l) % 2 == 0:
        print("Human")
    else:
        print("Alien")

creat(input())