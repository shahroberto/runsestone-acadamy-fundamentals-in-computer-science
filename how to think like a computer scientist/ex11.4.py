qbfile = open("qbdata.txt", "r")

for aline in qbfile:
    values = aline.split()
    # print values
    print'QB', values[0], values[1], 'had a rating of ', values[10]

qbfile.close()
