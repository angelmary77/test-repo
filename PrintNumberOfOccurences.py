
"""Find input string occurances"""
def getInputstringOccurences(inputString):
    inputOccurences = {}
    for i in inputString:
        if i in inputOccurences:
            inputOccurences[i] += 1
        else:
            inputOccurences[i] = 1
    return inputOccurences

"""Find input word occurances"""
def getWordOccurences(inputString):
    words = inputString.split()
    unwanted_chars = ".,-_"
    wordfreq = {}
    for raw_word in words:
        word = raw_word.strip(unwanted_chars)
        if word not in wordfreq:
            wordfreq[word] = 0
        wordfreq[word] += 1
    return wordfreq


inputString = raw_input("Enter some value: ")
print getWordOccurences(inputString)