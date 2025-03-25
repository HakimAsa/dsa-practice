#solution for an integer being palindrome in python

def is_palindrome(x):
    if(isinstance(x, int)==False or x < 0):
        return False
    x = str(x)
    x = ''.join(e for e in x if e.isalnum()).lower()
    return x == x[::-1]

#implementation with two pointers for optimization
def is_palindrome_with_two_pointers(x:int)->bool:
    if not isinstance(x, int):
        return False
    x = str(x)
    left = 0
    right = len(x) - 1
    while left < right:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1
    return True

#implementation without built-in func for better optimization
def is_palindrome_without_built_in(x:int)->bool:
    if not isinstance(x, int) or x < 0:
        return False
    reverseNum = 0
    temp = x
    while temp != 0:
        digit = temp % 10
        reverseNum = reverseNum * 10 + digit
        temp //= 10
    return x == reverseNum

# test cases for is_palindrome

print(is_palindrome(121))  # True
print(is_palindrome('121'))  # False
print(is_palindrome(-121))  # Flase
print(is_palindrome(10))  # Flase

# test cases for is_palindrome_with_two_pointers
print("------------ is_palindrome_with_two_pointers ------------")
print(is_palindrome_with_two_pointers(121))  # True
print(is_palindrome_with_two_pointers('121'))  # False
print(is_palindrome_with_two_pointers(-121))  # Flase
print(is_palindrome_with_two_pointers(10))  # Flase

# test cases for is_palindrome_without_built_in

print("------------ is_palindrome_without_built_in ------------")
print(is_palindrome_without_built_in(121))  # True
print(is_palindrome_without_built_in('121'))  # False
print(is_palindrome_without_built_in(-121))  # Flase
print(is_palindrome_without_built_in(10))  # Flase
