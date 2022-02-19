import csv
from datetime import datetime

CGREY = "\33[90m"
CGREEN = "\33[32m"
CYELLOW = "\33[33m"
CEND = "\33[0m"
CBOLD = "\033[1m"
CITALIC = "\33[3m"


def wordle():
    printRules()
    wordOfTheDay = pickWordOfTheDay()
    allowedGuesses = 5
    while True:
        if allowedGuesses == 0:
            print("You have no guesses left :(")
            break

        guess = input("Enter a 5-letter word (5 guesses): ").upper()

        if len(guess) != 5:
            print("Plesae enter a 5 letter word.")
            continue
        if not matchedLetters(guess, wordOfTheDay):
            allowedGuesses -= 1
            continue
        if guess == wordOfTheDay:
            print(f"Congrats! You got the word right! {wordOfTheDay.capitalize()}")
            break


def printRules():
    print(f"{CBOLD}LEGEND:{CEND}")
    print(f"{CITALIC}{CGREEN}\t you guessed right this letter!{CEND}")
    print(f"{CITALIC}{CYELLOW}\t you guessed right but in the wrong place...{CEND}")
    print(f"{CITALIC}{CGREY}\t is not exists in the word.{CEND}")


# letters check
def matchedLetters(guess, wordOfTheDay):
    isValid = True
    print("-------------")
    for i in range(len(wordOfTheDay)):
        if guess[i] == wordOfTheDay[i]:
            print(f"{CBOLD}{CGREEN}{guess[i]}{CEND} ", end="")
        elif guess[i] in wordOfTheDay:
            print(f"{CBOLD}{CYELLOW}{guess[i]}{CEND} ", end="")
            isValid = False
        else:  # guess[i] not in wordOfTheDay
            print(f"{CBOLD}{CGREY}{guess[i]}{CEND} ", end="")
            isValid = False
    print("\n-------------")
    return isValid


# pick the word of the day: prints
def pickWordOfTheDay():
    allWordsByDate = dict()
    nowDateFormatted = datetime.now().strftime("%b %d %Y")
    with open("wordle_list.csv", newline="") as csvfile:
        wordlist = csv.reader(csvfile)
        for word in wordlist:
            allWordsByDate[word[0]] = word

    date, id, word = allWordsByDate[nowDateFormatted]
    print(f"{CBOLD}Word of the day: {date}, #{id}.{CEND}")
    return word


wordle()
