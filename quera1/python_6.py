def hanoi(x, source, auxiliary, target):
    if x == 1: 
        print(f"{source}>{target}")
        return

    hanoi(x - 1, source, target, auxiliary)

    print(f"{source}>{target}")

    hanoi(x - 1, auxiliary, source, target)

x = int(input())
hanoi(x, 'A', 'B', 'C')
