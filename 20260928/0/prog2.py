l1 = list(range(5, 16))
l2 = [chr(c) for c in range(ord('a'), ord('k') + 1)]
l1[4:8] = l2[-5:]
print(l1, l2)
