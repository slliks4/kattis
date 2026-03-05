# n = int(input())
# numbers = []

# if 2 <= n <= (2*(10**5)):
#     for i in range(n):
#         lines = input().split()
#         a = int(lines[0])
#         b = int(lines[1])

#         if 0 <= a <= (2*(10**5)) and 0 <= b <= (2*(10**5)):
#             numbers.append(a)
#             numbers.append(b)
#         else:
#             break

#     possible_answers = []

#     for i in range(len(numbers)):
#         test_number = numbers[i]
#         bundle = []

#         k = 0
#         while k <= len(numbers) - 1:
#             if (numbers[k] <= test_number <= numbers[k+1]):
#                 bundle.append(test_number)

#             k += 2

#         if bundle.count(numbers[i]) == 3:
#             possible_answers.append(numbers[i])

#     if len(possible_answers) > 0:
#         print(f"{n}", min(possible_answers))
#     else:
#         print("bad news")


n = int(input())
low = 0
high = 2 * 10**5

for i in range(n):
    lines = input().split()
    a = int(lines[0])
    b = int(lines[1])

    if a > low:
        low = a
    if b < high:
        high = b

if low <= high:
    print(high - low + 1, low)
else:
    print("bad news")
