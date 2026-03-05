n,h = map(int, input().split())

game={}

for i in range(1,h+1):
    game[i] = []

for i in range(n):
    val = int(input())

    if i % 2 == 0:
        for j in range(val):
            game[h-j].append("X")

    if i % 2 != 0:
        for j in range(val):
            game[j+1].append("X")

out = []
for i in game:
    out.append(len(game[i]))

answer = min(out)
print(answer, out.count(answer))
