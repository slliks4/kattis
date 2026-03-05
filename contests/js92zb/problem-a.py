n = int(input())
p = int(input())
x = input().split()

newX = []

# New list
for i in x:
    newX.append(int(i)-p)

pfs = [0]
min = 0

for i in range(1, len(newX)-1):
    ans = (int(newX[i]) - p) - int(newX[i - 1])
    pfs.append(ans)
    if (ans < min):
        min = int(newX[i])

print(min, pfs)
