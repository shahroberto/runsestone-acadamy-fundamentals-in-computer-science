"""Simulate Hot potato using a queue."""

from pythonds.basic.queue import Queue


def hotPotato(namelist, num):
    """Simulate the Hot potato Game."""
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


def main():
    """Make main body of script."""
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))


if __name__ == "__main__":
    """Run on main."""
    main()
