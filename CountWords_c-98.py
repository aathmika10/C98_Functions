def countWords():
    fileName=input("Enter the name of the file: ")
    numberOfWords=0
    f=open(fileName,'r')
    for line in f:
        words=line.split()
        numberOfWords=numberOfWords+len(words)

    print("number of words in the file: ", numberOfWords)


countWords()