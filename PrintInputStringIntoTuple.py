string = raw_input("Enter any value with comma seperated: ")
Tpl= tuple(x.strip() for x in string.split(','))
print Tpl

