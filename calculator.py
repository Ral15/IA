import fileinput

# read input
lines = []
for line in fileinput.input():
	lines.append(line)

ans = 0
for line in lines:
	ans += int(line)

print(ans)