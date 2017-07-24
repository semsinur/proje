# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

num = 600851475143
a = 1
max = 0
for i in range(2,int(num ** 0.5)):
    if(num % i == 0):
        num /= i
        a = i
    if(a > max):
        max = a
print(max)
