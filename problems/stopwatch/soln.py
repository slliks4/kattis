n = int(input())

times = []

for i in range(n):
    time = int(input())
    times.append(time)

if n % 2 != 0:
    print("still running")
else:
    answer = 0
    for j in range(len(times) - 1, -1, -2):
        answer += (times[j]-times[j-1])

    print(answer)
