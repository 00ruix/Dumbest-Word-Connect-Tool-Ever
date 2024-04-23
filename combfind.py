import random

emptySpace = 0
letters = []

askLetters = True

while askLetters: #get letters from user
    print("Letters : ", letters)
    inp = input("enter letter: ")
    if inp != "end":
        letters.append(inp)
    else:
        askLetters = False

emptySpace = input("Number Of Tries: ")

#print(letters)

tried = []

def searchInFile(word): #needs work
    with open("words", 'r') as file:
        cont = file.read()

        if word in cont:
            print(word)
        else:
            pass
           # print("NOT IN CONT", word)

for i in range(int(emptySpace)):
    random.shuffle(letters)
    if ".".join(letters) in tried:
       # print("PASSED | |       ", tried)
        pass
    else:
        tried.append(".".join(letters))

        print(i + 1,"       ", " || ", " | ".join(letters))

#        searchInFile("".join(letters))



