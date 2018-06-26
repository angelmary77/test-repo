
def getSumOfNumbers(nums):
    sum = 0
    for num in nums:
        sum = sum + int(num)
    return  sum

num1 = raw_input("Enter first set of numbers: ")
num2 = raw_input("Enter second set of numbers: ")

SumOfNumber1 = getSumOfNumbers(num1)
SumOfNumber2 = getSumOfNumbers(num2)

if  SumOfNumber1 > SumOfNumber2:
    print "Sum of {0} is greater than Sum of {1}" .format(num1, num2)
else:
    print "Sum of {1} is greater than Sum of {0}" .format(num1, num2)