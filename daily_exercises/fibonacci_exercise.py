
def fibonacci(n):
    n1 = 0
    n2 = 1
    if n == 0:
        return n1
    elif n == 1:
        return n2
    else:
        for i in range(1, n):
            next = n1 + n2
            print(n1)
            n1 = n2
            n2 = next
        return n2

n = int(input("enter n:"))
print(fibonacci(n))