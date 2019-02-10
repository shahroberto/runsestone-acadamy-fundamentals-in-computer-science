"""Examine the O(n) of list functions."""
from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l2 = []
    for i in range(1000):
        l2.append(i)


def test3():
    l3 = [i for i in range(1000)]


def test4():
    l4 = list(range(1000))


def test5():
    pass


def main():
    t1 = Timer("test1()", "from __main__ import test1")
    print("concat ", t1.timeit(number=1000), "milliseconds")
    t2 = Timer("test2()", "from __main__ import test2")
    print("append ", t2.timeit(number=1000), "milliseconds")
    t3 = Timer("test3()", "from __main__ import test3")
    print("comprehension ", t3.timeit(number=1000), "milliseconds")
    t4 = Timer("test4()", "from __main__ import test4")
    print("list range ", t4.timeit(number=1000), "milliseconds")
    t5 = Timer("test5()", "from __main__ import test5")
    print("empty function ", t5.timeit(number=1000), "milliseconds")


if __name__ == "__main__":
    main()
