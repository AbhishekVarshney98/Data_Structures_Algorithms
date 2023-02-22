def sumofdigits(n):
    assert n>=0 and int(n)==n, "number should be non-negative integer"
    if n==0:
        return 0
    return int(n%10) + sumofdigits(int(n/10)) # sumofdigits(n//10) can also be used

print(sumofdigits(104))
print(sumofdigits(-104))
