def printFunction(name):
    print "Hello " + name + '. ' + "Have a good Day!"
    return

def addition(a, b):
    c =  a + b
    return c

def subtraction(a, b):
    c = a - b
    return c


''' Writing of code in module file itself'''
printFunction("Mary")
print addition(90, 10)
print subtraction(addition(40, 10), 2)