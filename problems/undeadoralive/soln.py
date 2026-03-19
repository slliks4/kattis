line = input()

smiley_face_count = 0
frown_face_count = 0

for i in range(len(line)):
    if line[i] == ":":
        if len(line) != i+1:
            if line[i+1] == ")":
                smiley_face_count += 1
            elif line[i+1] == "(":
                frown_face_count += 1

if frown_face_count == 0 and smiley_face_count > 0:
    print("alive")
elif frown_face_count > 0 and smiley_face_count == 0:
    print("undead")
elif frown_face_count > 0 and smiley_face_count > 0:
    print("double agent")
else:
    print("machine")
