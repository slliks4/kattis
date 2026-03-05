r, c = map(int, input().split())

out = {}

for _ in range(r):
    s = input()

    for i in range(len(s)):
        if s[i] != ".":
            out[i] = s[i]

answer = ""

for i in range(c):
    answer += out[i]

print(answer)
