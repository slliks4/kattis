letters = 'abcdefghijklmnopqrstuvwxyz'

n = int(input())
final_output = []

for i in range(n):
    phrase = input().strip().lower()
    missing = letters

    for ch in phrase:
        if ch in letters:
            missing = missing.replace(ch, '')

    if missing == '':
        final_output.append('pangram')
    else:
        final_output.append('missing ' + missing)

for line in final_output:
    print(line)
