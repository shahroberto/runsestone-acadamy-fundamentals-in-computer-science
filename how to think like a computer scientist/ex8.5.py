def seq3np1(n):
    """Print the 3n+1 seq from n, terminating when it reaches 1."""
    count = 0;
    while n != 1:
        print() ,
        if n % 2 == 0:      # n is even
            n = n // 2
        else:               # n is odd
            n = n*3 + 1
        count += 1
    print(n)                # the last print is always 1
    print("It took %d iterations to complete." % (count))

seq3np1(int(input("Enter a starting number: \n>")))
