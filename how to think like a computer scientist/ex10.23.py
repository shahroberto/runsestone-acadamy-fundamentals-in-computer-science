nested = ["hello", 2.0, 5, [10,20]]
innerlist = nested[3]
print(innerlist)
item = innerlist[1]
print(item)

print(nested[3][1])

song = "The rain in spain ..."
wds = song.split()
print(wds)

wds = song.split('ai')
print(wds)

wds = ["red", "blue", "green"]
glue = ";"
s = glue.join(wds)
print s
print wds

print("***".join(wds))
print("".join(wds))

xs = list("Crunchy Frog")
print(xs)
