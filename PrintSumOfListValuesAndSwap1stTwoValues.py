InputString =  raw_input("Enter any numbers: ")

Lst = map(int, list(InputString))
print "The given inputsting's List is: {0}".format(Lst)
sum = 0
for x in Lst:
    sum = sum + x
print 'Sum of the List {0} is: {1}'.format(Lst, sum)

Lst[0], Lst[1] = Lst[1], Lst[0]
print Lst



