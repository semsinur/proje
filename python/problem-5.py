# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

s = 1
for i in range(20, 1000000000, 20):
    if (s == 0):
        break
    for j in range(11, 21):
        if(i % j != 0):
            break
        if(j == 20):
            print(i)
            s = 0
