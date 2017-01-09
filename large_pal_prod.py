def largest_palindrome(n):
    upper_limit = 10**n - 1
    lower_limit = 10**(n-1) - 1
    largest = 0
    for a in range(upper_limit, lower_limit, -1):
        for b in range(upper_limit, lower_limit, -1):
            prod = a*b
            if prod < largest:
                break
            if (is_palindrome(prod)):
                largest = prod
    print largest % 1337
    
            
def is_palindrome(n):
    return str(n) == str(n)[::-1]
if __name__=='__main__':
    for n in range(1,9):
        print n, largest_palindrome(n)
