a = int(input("enter the number"))


def iteration(a):
    factor = 1
    for i in range(1, a+1):
        factor *= i

    return factor


result = iteration(a)
print(f"the factors are {result}")
