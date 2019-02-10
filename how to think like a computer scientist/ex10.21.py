def primes_upto(n):
    """ Return a list of all prime numbers less than n. """
    result = []
    for i in range(2,n):
        if is_prime(i):
            result.append(i)
    return result

def is_prime(n):
    """ Returns True if n is prime. """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

def main():
    number = int(raw_input("Enter a number to see all primes less than said number:\n>"))
    print(primes_upto(number))

main()
