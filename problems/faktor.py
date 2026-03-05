n = input().split()

a = int(n[0])
i = int(n[1])

if (1 <= i <= 100) and (1 <= a <= 100):
    b = ((i-1) * a) + 1
    print(b)
