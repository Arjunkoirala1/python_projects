def hanoi(n, a, b, c):
    if (n == 1):
        print("move disk 1 from rod{} to rod{}".format(a, c))
        return
    hanoi(n-1, a, b, c)
    print("move disk {} from rod{} to rod{}".format(n, a, b))
    hanoi(n-1, c, a, b)


disk = int(input("enter the number of disks:"))
hanoi(disk, "A", "B", "C")
