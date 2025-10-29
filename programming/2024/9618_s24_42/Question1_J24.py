def ReadWords(pFileName):
    global WordArray
    global NumberWords
    try:
        with open(pFileName, "r") as file:
            content = file.read()
            lines = content.split("\n")
        for line in lines:
            WordArray.append(line)
        NumberWords = len(WordArray) - 1
        Play()

    except IOError:
        print("Error: File not found")

def Play():
    global WordArray
    global NumberWords
    user_ans = []  # 1D array of type STRING
    correct_num = 0
    print(f"The main word is {WordArray[0]}")
    print(f"There are {NumberWords} answers.")
    answer = input("Enter a word to guess or enter 'no' to stop guessing ").lower()
    while answer != "no":
        user_ans.append(answer)
        answer = input("Enter a word to guess or enter 'no' to stop guessing ").lower()

    for word in user_ans:
        if word in WordArray[1: len(WordArray)]:
            correct_num += 1
            WordArray[WordArray.index(word)] = ""

    print(f"You got {round(((correct_num/NumberWords)*100))} percent of the answers!")

    for word in WordArray[1: len(WordArray)]:
        if word != "":
            print(f"You did not get the answer: {word}")

# main
WordArray = []  # 1D array of type STRING, GLOBAL
NumberWords = 0  # INTEGER, GLOBAL

choice = input("Choose your difficulty: easy, medium, hard : ").lower().capitalize()
ReadWords(choice+".txt")
