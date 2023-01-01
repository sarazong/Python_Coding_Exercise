# 1. Sherlock and Anagrams (https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_r=internal-search)
def sherlockAndAnagrams(s):
    count=0
    # the different lengths a substring could have, from "1 to len(s)-1"
    # the last number is excluded, so the end of the range is "len(s)" instead of "len(s)-1"
    for shift in range(1, len(s)):
        # if a substring contains only one letter, indices for the substring would be "i:i+1",
        # until the end of the string, the indices would be "len(s)-1:len(s)"
        # if a substring contains two letters, indices for the substring would be i:i+2
        # until the end of the string, the indices would be "len(s)-2:len(s)"
        # ...
        # the last number is excluded, so the end of the range is "len(s)-shift+1" instead of "len(s)-shift"
        sub_strings = [s[i:i+shift] for i in range(len(s)-shift+1)]

        # sort all the substrings to identify substrings that have the same letters
        sub_strings_sorted = [sorted(ss) for ss in sub_strings]
        for i in range(len(sub_strings_sorted) - 1):
            for j in range(i+1, len(sub_strings_sorted)):
                if sub_strings_sorted[i] == sub_strings_sorted[j]:
                    count += 1
    return(count)


# 2. Pairs (https://www.hackerrank.com/challenges/pairs/problem)
def pairs(k, arr):
    count = 0
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr), 1):
            if abs(arr[i] - arr[j]) == k:
                count += 1
    return(count)


# 3. Absolute Permutation (https://www.hackerrank.com/challenges/absolute-permutation/problem)
def absolutePermutation(n, k):
    # if k is 0, there is always the permutation of numbers and their positions being exactly the same
    if k == 0:
        p = list(range(1, n+1))
        return p
    # when k is no 0, permutation is only possible when n numbers can be evenly divided into n/(2k) groups
    elif n%(2*k) == 0:
        start=0
        end=k
        p = list(range(1, n+1))
        while end < n+1:
            if end%(2*k) != 0:
                for i in range(start, end):
                    p[i] += k
            else:
                for i in range(start, end):
                    p[i] -= k
            start += k
            end += k
        return p
    else:
        return [-1]


# 4. Non-Divisible Subset (https://www.hackerrank.com/challenges/non-divisible-subset/problem)
def nonDivisibleSubset(k,s):
    result = {}
    count = 0
    for i in range(len(s)):
        key = s[i] % k
        result[key] = result.get(key, 0) + 1

    for key in range(1, math.ceil(k/2)):
        count += max(result.get(key, 0), result.get(k-key, 0))
    if result.get(0, 0) != 0:
        count += 1
    if k % 2 == 0 and result.get(k/2, 0) != 0:
        count += 1
    return count


# 5. Multiples of 3 or 5
# Find the sum of all the multiples of 3 or 5 below 1000.
answer = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        answer += i
answer


# 6. Even Fibonacci numbers
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
fibon_seq = [1, 2]
while fibon_seq[-1] < 4000000:
    fibon_seq.append(fibon_seq[-1] + fibon_seq[-2])
fibon_seq = fibon_seq[ : -1]
# OR fibon_seq.pop(-1)
print(fibon_seq)
len(fibon_seq)

answer = 0
for i in fibon_seq:
    if i % 2 == 0:
        answer += i
answer


# 7. Largest prime factor
# What is the largest prime factor of the number 600851475143 ?
import math

def prime_factor(x):
    factor_list = []
    for i in range(2, round(math.sqrt(x)) + 1):
        if x % i != 0:
            next
        else:
            while x % i == 0:
                x /= i
            factor_list.append(i)
    if x > 1:
        factor_list.append(round(x))
    return factor_list, factor_list[-1]


# 8. Largest palindrome product
# Find the largest palindrome made from the product of two 3-digit numbers.
palindromes = []
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        product = i * j
        if list(str(product)) == list(reversed(str(product))):
            palindromes.append(product)
largest = max(palindromes)
print(largest)


# 9. Smallest multiple
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math
def smallest_multiple(x, y):
    smallest_multiple = {}
    multiple = 1

    for n in range(x, y + 1):
        prime_factors = {}
        while (n % 2 == 0):
            prime_factors[2] = prime_factors.get(2, 0) + 1
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                prime_factors[i] = prime_factors.get(i, 0) + 1
                n //= i
        if (n > 1):
            prime_factors[n] = prime_factors.get(n, 0) + 1

        for key, value in prime_factors.items():
            smallest_multiple[key] = max(prime_factors[key], smallest_multiple.get(key, 0))

    for key, value in smallest_multiple.items():
        multiple *= (key ** value)
    return multiple


# 10. Sum square difference
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def difference(x, y):
    sum_of_num = 0
    sum_of_square = 0
    for i in range(x, y+1):
        sum_of_num += i
        sum_of_square += i ** 2
    difference = sum_of_num ** 2 - sum_of_square
    return difference
