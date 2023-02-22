def power(base,exp):
    assert int(exp)==exp, "exponent must be an integer"
    if exp==0:
        return 1
    elif exp<0:
        return 1/base * power(base, exp+1)
    return base * power(base, exp-1)

print(power(2,8))
print(power(0,8))
print(power(4,-1))
