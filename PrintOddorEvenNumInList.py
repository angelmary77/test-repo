InputString =  raw_input("Enter Numbers: ")

Lst = map(int, list(InputString))
print Lst

OddList = []
EvenList = []
for x in Lst:
    if (x % 2) == 0:
        OddList.append(x)
    else:
        EvenList.append(x)

print "Odd list is: ", OddList
print "Even list is: ", EvenList

