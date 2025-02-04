def kelaasor_shirt(choice, list_shirt):
    sizes = list(list_shirt.keys())
    output = []
    for i in range(len(choice)):
        key = choice[i]
        if key in list_shirt and list_shirt[key] > 0:
            list_shirt[key] -= 1
            output.append(key) 
        else:
            index = sizes.index(key) if key in sizes else -1
            if index != -1:
                for local in [1, -1, 2, -2]:
                    new_index = index + local
                    if 0 <= new_index < len(sizes):
                        new_key = sizes[new_index]
                        if new_key in list_shirt and list_shirt[new_key] > 0:
                            list_shirt[new_key] -= 1
                            output.append(new_key)
                            break
                else:
                    output.append("No Shirt")
            else:
                    output.append("No Shirt")
    return output





number_shirt = list(map(int, input().split()))
size = ["S", "M", "L", "XL", "XXL"]
list_shirt = dict(zip(size, number_shirt))
# print(list_shirt)
person = int(input())
# print(person)
choice = []
for i in range(person):
    input_size = input().upper()
    choice.append(input_size)
# print(choice)

result = kelaasor_shirt(choice, list_shirt)
for res in result:
    print(res)