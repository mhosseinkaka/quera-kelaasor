number_shirt = list(map(int, input().split()))
size = ["S", "M", "L", "XL", "XXL"]
list_shirt = dict(zip(size, number_shirt))
print(list_shirt)
person = int(input())
print(person)
choice = []
for i in range(person):
    input_size = input().upper()
    choice.append(input_size)
print(choice)

def assign(choice, list_shirt):
    