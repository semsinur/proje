# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def prime(n):
    for i in range(2, int(n ** 0.5)+1):
        if(n % i == 0):
            return False
    else:
        return True
num = 0
j = 1
while(num != 10001):
    j += 1
    if prime(j):
        num += 1
print(j)
