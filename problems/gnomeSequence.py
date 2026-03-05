n = int(input())
answer = []

if (0 < n < 30):
    for _ in range(n):
        x = input().split()

        x_first = int(x[0])
        x_sencond = int(x[1])
        x_last = int(x[2])

        if (x_first > 100 or x_sencond > 100 or x_last > 100):
            break

        if (x_first < x_sencond) and (x_sencond < x_last):
            answer.append("Ordered")
        elif (x_first > x_sencond) and (x_sencond > x_last):
            answer.append("Ordered")
        else:
            answer.append("Unordered")

print("Gnomes:")
for i in answer:
    print(i)
