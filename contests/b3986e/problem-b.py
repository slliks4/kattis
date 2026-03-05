n = int(input())
output_answer = []

control = {
    "fishing": "alice",
    "golf": "bob",
    "hockey": "charlie"
}

games = ["fishing", "golf", "hockey"]
names = ["alice", "bob", "charlie"]

for i in range(n):
    current = []
    txt = input().split()

    for j in range(len(names)):
        # Check what game and the player name
        if (names[j] in txt):
            # Check who currently is with the game and assign reasonably
            if games[0] in txt:
                currently_held_by = control.get(games[0])
                if currently_held_by != names[j]:
                    output_answer.append(f"{names[j]} borrows {games[0]} from {currently_held_by}")
                    control[games[0]] = names[j]
                else:
                    output_answer.append(f"{names[j]} already has {games[0]}")

            elif games[1] in txt:
                currently_held_by = control.get(games[1])
                if currently_held_by != names[j]:
                    output_answer.append(f"{names[j]} borrows {games[1]} from {currently_held_by}")
                    control[games[1]] = names[j]
                else:
                    output_answer.append(f"{names[j]} already has {games[1]}")

            elif games[2] in txt:
                currently_held_by = control.get(games[2])
                if currently_held_by != names[j]:
                    output_answer.append(f"{names[j]} borrows {games[2]} from {currently_held_by}")
                    control[games[2]] = names[j]
                else:
                    output_answer.append(f"{names[j]} already has {games[2]}")


for j in output_answer:
    print(j)
