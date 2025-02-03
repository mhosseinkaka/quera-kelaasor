def kelaasor_shirt(choice, list_shirt):
    for i in range(len(choice)):
        
        key = choice[i]
        if list_shirt[key] > 0:
            list_shirt[key] -= 1
            print(list_shirt[key]) 
        else:
            if  list_shirt[choice[i + 1]] > 0:
                list_shirt[choice[i + 1]] -= 1
                print(list_shirt[choice[i + 1]])
            else:
                if list_shirt[choice[i - 1]] > 0:
                    list_shirt[choice[i - 1]] -= 1
                    print(list_shirt[choice[i - 1]])
                else:
                    if list_shirt[choice[i + 2]] > 0:
                        list_shirt[choice[i + 2]] -= 1
                        print(list_shirt[choice[i + 2]])
                    else:
                        if list_shirt[choice[i - 2]] > 0:
                            list_shirt[choice[i - 2]] -= 1
                            print(list_shirt[choice[i - 2]])
                        else:
                            list_shirt[key] = "No-Shirt"


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
for key, value in result.items():
    print(value)