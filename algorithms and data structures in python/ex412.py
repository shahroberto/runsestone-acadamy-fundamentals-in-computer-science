"""Dynamic Programming.

Calculate the smallest change given a coin set with three different methods.
The first method uses a recursive call: extremely inefficient because it looks
at the same option multiple times.  The second method uses caching/memoization
to store the minCoins for a given change set while running through algorithm
1.  The last function uses dynamic programming to systematically work up from
1 penny to the amount of change while storing the change values for each value
as it increments.
"""


def recMC(coinValueList, change):
    """Calculate the smallest change."""
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins


def recDC(coinValueList, change, knownResults):
    """Calculate the smallest change using memoization/caching."""
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins


def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    """Calculate smallest change using dynamic programming."""
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


def printCoins(coinsUsed, change):
    """Print the coins used to make change."""
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


def main():
    """Execute main code."""
    # Recursive form:
    # print(recDC([1, 5, 10, 25], 63))

    # Memoizing/caching form:
    # print(recMC([1, 5, 10, 25], 63, [0] * 64))

    # Dynamic form:
    amnt = 6
    clist = [1, 5, 10, 25]
    coinsUsed = [0] * (amnt + 1)
    coinCount = [0] * (amnt + 1)

    print("Making change for", amnt, "requires")
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins")
    print("They are:")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows:")
    print(coinsUsed)


if __name__ == "__main__":
    main()
