def message(list_char):
    list_final = []
    i = 0
    while i < len(list_char):
        if list_char[i] != " ":
            number = 1
            next_char = i
            while (next_char + 1) < len(list_char) and list_char[next_char] == list_char[next_char + 1]:
                next_char += 1
                number += 1
            list_final.append(list_char[i])
            list_final.append(number)
            i = next_char + 1
        else:
            list_final.append(list_char[i])
            i += 1
    return list_final
        

text = list(input())
result = ''.join(map(str, message(text)))
print(result)