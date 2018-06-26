
def writeDataInFile(newFile):
    """Writting text into a file"""
    newFile = open(newFile, 'w+')
    for i in range(5):
        newFile.writelines("This line is: %d\r\n" % (i + 1))
    newFile.close()
    return newFile

def appendDataInFile(newFile):
    """Appending text into a file"""
    newFile = open(newFile, 'a')
    newFile.write("This is appended line")
    newFile.close()
    return newFile

# Reading data from the file
writeDataInFile('Test.txt')
print open("Test.txt").read()

appendDataInFile('Test.txt')
print open("Test.txt").read()




