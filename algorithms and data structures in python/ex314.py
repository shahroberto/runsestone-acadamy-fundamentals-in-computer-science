"""Analyze timing of printing tasks using queues and a simulation."""

from pythonds.basic.queue import Queue
import random


class Printer:
    """Manage printer and track if it has a current task."""

    def __init__(self, ppm):
        """Initialize printer properties."""
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        """Count down time to print a task."""
        if self.currentTask is not None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        """Printer is busy."""
        if self.currentTask is not None:
            return True
        else:
            return False

    def startNext(self, newtask):
        """Start the next task."""
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    """Keep track of the task list."""

    def __init__(self, time):
        """Initialize type."""
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        """Return timestamp."""
        return self.timestamp

    def getPages(self):
        """Return number of pages."""
        return self.pages

    def waitTime(self, currenttime):
        """Return waitime."""
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute, numstudents):
    """Run the Simulation."""
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask(numstudents):
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait {:6.2f} secs {:3d} tasks remaining.".format(
        averageWait, printQueue.size()))


def newPrintTask(numstudents):
    """Create new printing task."""
    prob = 1 // ((numstudents * 2) / (3600))
    num = random.randrange(1, prob + 1)
    if num == prob:
        return True
    else:
        return False


def main():
    """Make main body of script."""
    numstudents = int(input("Enter the number of students in the lab:\n>"))
    for i in range(10):
        simulation(3600, 5, numstudents)
    print("-" * 50)
    for i in range(10):
        simulation(3600, 10, numstudents)


if __name__ == "__main__":
    """Run on main."""
    main()
