answer = []
while True:
    s = input().strip()

    if s == "#":
        break

    last_char = s[-1]

    count = 0
    for i in s:
        if i == '1':
            count += 1

    isEven = count % 2 == 0

    if last_char == "o":
        if isEven:
            answer.append(s[:-1] + "1")
        else:
            answer.append(s[:-1] + "0")

    else:
        if isEven:
            answer.append(s[:-1] + "0")
        else:
            answer.append(s[:-1] + "1")

for t in answer:
    print(t)
