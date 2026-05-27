#project Euler #4 - largest palindrome of two 3 - digit numbers 
# a palindrome is a number that is the same backwards and forwards, like 101 or 990099

import time

def is_palindrome(val):
    val = str(val)
    if val == val[::-1]:
        return(True)
    else:
        return(False)
#def is_palindrome(val):
 #   return str(val) == str(val)[::-1]
 

#go through 101~999 and add the palindrome to the list of palindromes 

palindromes = [] 

for i in range(101,1000):
    for j in range (101,1000):
        if is_palindrome(str(i)+str(j)):
            palindromes.append(str(i)+str(j))

print(palindromes)
print(max(palindromes))


