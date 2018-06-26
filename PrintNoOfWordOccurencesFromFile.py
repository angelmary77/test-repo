
fo = open("TestFO.txt", "wb")
fo.write(raw_input("Enter any stings or numbers: "))
fo.close()
file = open("TestFO.txt")
data = file.read()
words = data.split()
fo.close()

unwanted_chars = ".,-_"
wordfreq = {}
for raw_word in words:
    word = raw_word.strip(unwanted_chars)
    if word not in wordfreq:
        wordfreq[word] = 0
    wordfreq[word] += 1

print wordfreq



