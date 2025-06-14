a = int(input("Enter the number: "))


def factorial_recursive(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial_recursive(a - 1)


result = factorial_recursive(a)
print(f"Factorial of {a} is {result}")
