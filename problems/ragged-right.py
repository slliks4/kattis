import sys
sentence = sys.stdin.readlines()

paragraph_len = []

for paragraph in sentence:
    cleaned_paragraph = paragraph.replace("\n", "")
    paragraph_len.append(len(cleaned_paragraph))


max_lenght = max(paragraph_len)
answer = 0

if (paragraph_len[len(paragraph_len) - 1] != max_lenght):
    paragraph_len.remove(max_lenght)
    for i in range(len(paragraph_len) - 1):
        answer += (max_lenght - paragraph_len[i])**2
else:
    for i in range(len(paragraph_len)):
        answer += (max_lenght - paragraph_len[i])**2

print(answer)
