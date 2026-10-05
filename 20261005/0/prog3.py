from inspect import stack
def req(n): 
    if n == 0:
        return
    print(len(stack()))
    return req(n-1)
print(req(int(input())))
