n = input().split()

h = int(n[0])
w = int(n[1])
b = int(n[2])
c = int(n[3])

volume = h * w * b

if volume > c:
    print('SO MUCH SPACE')
elif volume == c:
    print('COZY')
else:
    print('TOO TIGHT')
