def factorial(n):
    assert n>=0 and int(n)==n, "Number should be non-negative integer"
    if n in [0,1]:
        return 1
    return n*factorial(n-1)

print(factorial(5))
print(factorial(6))
print(factorial(-1))
