input_line = input()

uniq_pairs = set()
for i in range(len(input_line) - 1):
    if not input_line[i].isalpha() or not input_line[i + 1].isalpha():
        continue

    uniq_pairs.add(input_line[i:i+2].lower())

print(len(uniq_pairs))
