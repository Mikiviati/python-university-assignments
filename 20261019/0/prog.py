import timeit

def f1():
    repeats, time = timeit.Timer(input()).autorange()

    print(f"Total time: {time} for {repeats} repeats")

def f2():
    inpt = set(input())
    cons = set("qwrtpsdfghjklzxcvbnm")
    vowels = set("eyuioa")
    print(cons)

    def letters_count():
        return len(inpt & cons), len(inpt & vowels)

    timer = timeit.Timer(letters_count)
    time, repeats = timer.autorange()

    print(f"Total time: {time} for {repeats} repeats")

def f3():
    words = {}
    for word in input().split():
        words[word] = words.get(word, 0) + 1
    
    print(words)

from collections import Counter

def f4():
    print(dict(Counter(input().split())))

def f5():
    text = input()

    def count_manual():
        words = {}
        for word in text.split():
            words[word] = words.get(word, 0) + 1
        return words

    def count_counter():
        return dict(Counter(text.split()))

    t1 = timeit.Timer(count_manual)
    t2 = timeit.Timer(count_counter)

    time1, repeats1 = t1.autorange()
    time2, repeats2 = t2.autorange()
    
    print(f"Time without 'Counter': {time1} for {repeats1} repeats")
    print(f"Time with 'Counter': {time2} for {repeats2} repeats")


def f6():
    return " ".join({w:1 for w in input().split()})

def f7():
    p = input()
    a, b = eval(input())

    eval(p, {"x":a, "y":b})
    eval(p, {"x":b, "y":a})

def f8():
    a = Counter(input().split())
    b = Counter(input().split())
    if (b - a):
        print("No")
    else:
        print("True")
