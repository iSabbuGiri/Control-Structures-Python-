def is_prime(x):
# only positive numbers are allowed and the smallest number is 2
    if (x > 1):
    # we start with the divisor 3
        divisor = 2
        for i in range(divisor, x):
            if(x % i ==0):
                return False
    else:
        return False

    return True
print (is_prime(3))                    
