"""Example 5.16 q. 2.

Set up a random experiment to test the difference between a binary
search and a binary recursive search on a list of integers.
"""

from timeit import Timer
import random
import matplotlib.pyplot as plt
from ex512 import quickSort

listlen = 1113
alist = random.sample(range(0, listlen * 10), listlen)
bintime = [None] * listlen
rbintime = [None] * listlen

print(alist)
quickSort(alist)
print(alist)

binwin = 0
rbinwin = 0

for pos in range(len(alist)):
    print("\nSearching for {} at position {} of {}:".
          format(alist[pos], pos, len(alist) - 1))
    t1 = Timer("binarySearchR({}, {}, 0, {})".
               format(alist, alist[pos], len(alist)),
               "from ex5163 import binarySearchR")
    rbintime[pos] = t1.timeit(number=1000)
    print("Seq: {:10.6f} ms".format(rbintime[pos]))
    t2 = Timer("binarySearch({}, {})".format(alist, alist[pos]),
               "from ex54 import binarySearch")
    bintime[pos] = t2.timeit(number=1000)
    print("Bin: {:10.6f} ms".format(bintime[pos]))

    if bintime[pos] < rbintime[pos]:
        binwin += 1
    else:
        rbinwin += 1

print("\nRecursive Binary search won {} times.\nBinary search won {} times.".
      format(rbinwin, binwin))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(rbintime, color='lightblue', label='Recursive Binary')
ax.plot(bintime, color='red', label='Binary')
ax.set_xlim(0, listlen)
ax.grid(True, zorder=5)
ax.set_title('Comparision between Seq and Bin search for {} items.'.
             format(len(alist)))
ax.set_ylabel("Time in ms")
ax.set_xlabel('Position of the item being searched for.')
plt.legend()
plt.show()
