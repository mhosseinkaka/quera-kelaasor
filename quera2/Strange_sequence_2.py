def get_pos(n):
    if n == 1:
        return "1"
    pos = 1  
    power = 0  
    while pos + len(str(10**power)) <= n: 
        pos += len(str(10**power))
        power += 1
    
    return str(10**power)[n - pos]  

n = int(input())
print(get_pos(n))