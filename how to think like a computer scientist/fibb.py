import time

numcycles = 40

# fibonacci sequence using only iteration
start = time.clock()
def itfibb(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

print "\nFibonacci sequence using iterative method for ", numcycles, " cycles is ", itfibb(numcycles), "\n"
marker = time.clock()
ittime = marker - start
print "\tTime taken for iterations: ", ittime, " seconds\n"

# fibonacci sequence using only recursion
def recfibb(n):
    recAns = []
    if n == 1 or n == 2:
        return 1
    else:
        return recfibb(n-1) + recfibb(n-2)

print "Fibonacci sequence using recursive method for ", numcycles, " cycles is ", recfibb(numcycles), "\n"
end = time.clock()
rectime = end - marker
print "\tTime taken for recursion: ", rectime, " seconds\n"
timediff = rectime - ittime
print "\tDifference between recursion and iterations: ", timediff, " seconds\n"
