import random
import math

def fib(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)


def getRandom(n):
    while True:
        temp = random.randrange(n)
        if math.gcd(temp, n) == 1:
            return temp


def Isprime(n):
    for i in range(20):
        a = getRandom(n)
        if(a ** (n-1)) % n != 1:
            return False
    return True

num = int(input("Give a number: "))
p = fib(num)
print(p)
boolean = Isprime(p)
if boolean == True:
    print("This is a prime number")
elif boolean == False:
    print("This is not a prime number")

