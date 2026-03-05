import statistics

no_entry_triggered = int(input())
no_exit_triggered = int(input())

entry_timestamps = input().split()
exit_timestamps = input().split()

answer = []

for i in range(no_entry_triggered):
    for j in range(no_exit_triggered):
        if (int(entry_timestamps[i]) < int(exit_timestamps[j])):
            answer.append(int(exit_timestamps[j]) - int(entry_timestamps[i]))

print(statistics.mode(answer))
