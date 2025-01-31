n = int(input())
if 1 <= n <= 19 and n % 2 != 0:
    for i in range(n):
        if i <= n // 2:
            print(' ' * ((n // 2 -i)), end="")
            m = (n // 2 -i)
            print('*' * (2 * i + 1), end="")
            print(' ' * 2 * m, end="")
            print('*' * (2 * i + 1))
        else:
            print(' ' * (i - (n // 2)), end="")
            z = i - (n // 2)
            print('*' * (2 * (n - i - 1) + 1), end="")
            print(' ' * 2 * z, end="")
            print('*' * (2 * (n - i - 1) + 1))