# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
# numbers is 9009 = 91 × 99.Find the largest palindrome made from the product of two 3-digit numbers.

num = 0
i = 999
while (i > 100):
    i -= 1
    j = i
    while (j > 100):
        j -= 1
        test = i * j
        if (test > num):
            s = str(i * j)
            if (s == s[::-1]):
                num = i * j
print(num)
