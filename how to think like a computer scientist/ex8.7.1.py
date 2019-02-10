def accumulatorCost():
    moreItems = True
    total = 0.0
    count = 0
    while moreItems:
        price = float(raw_input("Enter the cost of your item please ($CAD); enter 0 if finished:\n>"))
        if price != 0:
            total += price
            count += 1
            print "Subtotal: $%.2f" % (total)
        else:
            moreItems = False

    print "The total amount of items is: %d items." % (count)
    print "The total cost of items is: $%.2f." % (total)
    print "The average cost of each item is: $%.2f." % (total/count)

accumulatorCost()
