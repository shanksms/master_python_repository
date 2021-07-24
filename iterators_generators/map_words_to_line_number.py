from collections import defaultdict

words_line_map = defaultdict(list)
with open('words.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        words_line_map[word].append(idx)

print(words_line_map)