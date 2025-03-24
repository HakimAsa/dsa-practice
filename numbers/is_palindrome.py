#solution for an integer being palindrome in python

def is_palindrome(x):
    if(isinstance(x, int)==False or x < 0):
        return False
    x = str(x)
    x = ''.join(e for e in x if e.isalnum()).lower()
    return x == x[::-1]

# test cases

print(is_palindrome(121))  # True
print(is_palindrome('121'))  # False
print(is_palindrome(-121))  # Flase
print(is_palindrome(10))  # Flase
