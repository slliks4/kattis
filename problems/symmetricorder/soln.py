output = []
set_number = 0
control = True

while control:
    # Store just the even indexed words
    words = []
    # Stores Odd index words
    odd_words = []
    # Stores Even index words
    even_words = []

    n = int(input())

    if n <= 0:
        control = False
        break

    if n > 15:
        control = False
        break

    set_number += 1

    for i in range(n):
        word = input().replace(" ", "")

        if len(word) > 25:
            control = False
            break

        words.append(word)

    for j in range(0, len(words)):
        if (j % 2 == 0):
            even_words.append(words[j])
        else:
            odd_words.append(words[j])

    # Append Set number to output
    output.append(f"SET {set_number}")

    # Append Even Words to output
    for e in even_words:
        output.append(e)

    # Reverse odd Words and append to outpu
    for t in range((len(odd_words) - 1), -1, -1):
        output.append(odd_words[t])

for s in output:
    print(s)
