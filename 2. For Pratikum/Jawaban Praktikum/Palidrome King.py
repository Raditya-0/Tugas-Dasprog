def is_palindrom(s):
    reversed_s = s[::-1]
    return s == reversed_s

s = input()

if is_palindrom(s):
    print("Palindrome King!")
else:
    print("Bukan King!")