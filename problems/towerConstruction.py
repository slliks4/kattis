n = int(input())
x = input().split()

count = 1
i = 0
while i < len(x):
    if (i != len(x) - 1):
        if (int(x[i+1]) > int(x[i])):
            count += 1
    i += 1
print(count)
