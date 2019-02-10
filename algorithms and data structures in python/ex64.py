"""Examples of Trees."""


def treesAsLists():
    """Trees as a list of lists."""
    myTree = ['a', ['b', ['d', [], [], ], ['e', [], []]], ['c',
                                                           ['f', [], []], []]]

    print(myTree)
    print('left subtree = ', myTree[1])
    print('root = ', myTree[0])
    print('right subtree = ', myTree[2])


def BinaryTree(r):
    """Construct a list with a root node and two empty sublists (children)."""
    return [r, [], []]


def insertLeft(root, newBranch):
    """Insert a left branch to the tree."""
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    """Insert a right branch to the tree."""
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    """Retrieve the root value."""
    return root[0]


def setRootVal(root, newVal):
    """Set root."""
    root[0] = newVal


def getLeftChild(root):
    """Get left child."""
    return root[1]


def getRightChild(root):
    """Get Right child."""
    return root[2]


def main():
    """Execute main function."""
    # treesAsLists()
    r = BinaryTree(3)
    insertLeft(r, 4)
    insertLeft(r, 5)
    insertRight(r, 6)
    insertRight(r, 7)
    l = getLeftChild(r)
    print(l)

    setRootVal(l, 9)
    print(r)
    insertLeft(l, 11)
    print(r)
    print(getRightChild(getRightChild(r)))


if __name__ == "__main__":
    main()
