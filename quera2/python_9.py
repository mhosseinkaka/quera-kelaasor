def check(list1, list2):
    if len(list1) != len(list2):
        return("nooooooooooo")
    diff = [list2[i] - list1[i] for i in range(len(list1))]
    
    if len(set(diff)) == 1:
        return "YES"
    
    if len(set(diff)) == 2:
        if diff[1] - diff[0] == diff[1]:
            return "YES" 

    for i in range(1, len(diff)):
        if diff[i] != diff[i - 1]:
            return "NO"
            
    return "YES"


l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

print(check(l1, l2))