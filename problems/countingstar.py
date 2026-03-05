x = input().split()

m = int(x[0])
n = int(x[1])

new_index_list = []

for i in range(m):
    y = input()
    if len(y) > n:
        break

    for t in range(len(y)):
        if y[t] == '-':
            new_index_list.append({i: t})

print(new_index_list)
