x = int(input("enter any number"))
if (x <= 1):
    print("neither prime nor composite")

else:
    for i in range(2, x):
        if (x % i == 0):
            print("it is a composite number")
            break
    else:
        print("it is a prime number")
