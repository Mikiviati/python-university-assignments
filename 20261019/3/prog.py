

W = int(input())

words = {}
while line := input():
    formated_line = "".join(c if c.isalpha() else " " for c in line)

    for word in formated_line.split():
        if len(word) == W:
            words[word] = words.get(word, 0) + 1

if words:
    max_count = max(words.values())
    result = sorted(word for word, count in words.items() if count == max_count)
    print(*result)
