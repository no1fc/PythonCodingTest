n = int(input());

score = [];

for i in range(n):
    score.append(int(input()));

max = max(score);
min = min(score);

print(max-min);