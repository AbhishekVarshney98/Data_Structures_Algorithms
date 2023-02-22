# series : 0 1 1 2 3 5 8 13 21
def fibonacci(n):
    assert n>=0 and int(n)==n, "fibonacci should be non-negative integer"
    if n in [0,1]:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(-1))
