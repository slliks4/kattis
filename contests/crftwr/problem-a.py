import sys

n,m,q = map (int, input().split())

lines = sys.stdin.readlines()

questions_and_answers = {}
out = {}

for i in range(n, n+q):
    question, answer = lines[i].split()
    questions_and_answers[int(question)] = answer

for j in range(n):
    character = lines[j]
    count = 0
    for k in sorted(questions_and_answers):
        if character[k-1] == questions_and_answers[k]:
            count += 1
    out.setdefault(count, []).append(j+1)

answer = len(out[q])

if answer > 1:
    print("ambiguous")
    print(answer)
else:
    print("unique")
    print(out[q][0])
