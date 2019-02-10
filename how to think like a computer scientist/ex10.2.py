vocabulary = ["iteration", "selection", "control"]
numbersA = [17, 123]
empty = []
mixedlist = ["hello", 2.0, 5*2, [10, 20]]

print(numbersA)
print(mixedlist)
newlist = [numbersA, vocabulary]
print(newlist)

alist =  ["hello", 2.0, 5, [10, 20]]
print(len(alist))
print(len(['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]))

numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[2])
print(numbers[9 - 8])
print(numbers[-2])
print(numbers[len(numbers) - 1])

fruit = ["apple", "orange", "banana", "cherry"]
print("apple" in fruit)
print("pear" in fruit)

print([1, 2] + [3, 4])
print(fruit + [6, 7, 8, 9])

print([0] * 4)
print([1, 2, ["hello", "goodbye"]] * 2)

a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])

fruitz = ["banana", "apple", "cherry"]
print(fruitz)

fruitz[0] = "pear"
fruitz[-1] = "orange"
print(fruitz)

alistz = ['a', 'b', 'c', 'd', 'e', 'f']
alistz[1:3] = ['x', 'y']
print(alistz)

alisty = ['a', 'b', 'c', 'd', 'e', 'f']
alisty[1:3] = []
print(alisty)

alista = ['a', 'd', 'f']
alista[1:1] = ['b', 'c']
print(alista)
alista[4:4] = ['e']
print(alista)

a = ['one', 'two', 'three']
del a[1]
print(a)

alistb = ['a', 'b', 'c', 'd', 'e', 'f']
del alistb[1:5]
print(alistb)
