#check palindrome

def is_palindrome(input_string):
    if(input_string == input_string[::-1]):
        return True
    else:
        return False


print(is_palindrome("river"))
print(is_palindrome("redivider"))