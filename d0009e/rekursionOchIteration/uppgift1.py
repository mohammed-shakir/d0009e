


def bounce(n):
    if n == 0:
        print(n)
        return n
    else:
        print(n)
        bounce(n-1)
        print(n)

def bounce2(n):
    x = n
    for i in range(n+1):
        print(x)
        x = x-1

    for i in range(1, n+1):
        print(i)
        x = x+1

def tvarsumman(n):
    if n == 0:
        return n
    else:
        return n%10 + tvarsumman(n//10)

def tvarsumman2(n):
    list1 = []
    x = str(n)
    for i in x:
        list1.append(int(i))

    return sum(list1)

bounce(4)
#bounce2(4)
#print(tvarsumman(22))
#tvarsumman2(23)