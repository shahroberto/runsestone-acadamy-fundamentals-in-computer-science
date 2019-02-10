"""The tower of Hanoi."""


def moveTower(height, fromPole, toPole, withPole):
    """Move a tower."""
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fp, tp):
    """Move a disk."""
    print("Moving disk from", fp, "to", tp)


def main():
    """Make main body of script."""
    moveTower(3, "A", "B", "C")


if __name__ == "__main__":
    """Run on main."""
    main()
