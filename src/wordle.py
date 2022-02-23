from enum import Enum
from os import path
import csv
from datetime import datetime

CGREY = "\33[90m"
CGREEN = "\33[32m"
CYELLOW = "\33[33m"
CEND = "\33[0m"
CBOLD = "\033[1m"
CITALIC = "\33[3m"


def wordle():
  print_rules()
  wordOfTheDay = pick_word_of_the_day()
  allowedGuesses = 5
  while True:
    if allowedGuesses == 0:
      print("You have no guesses left :(")
      break

    guess = input("Enter a 5-letter word (5 guesses): ").upper()

    if len(guess) != 5:
      print("Plesae enter a 5 letter word.")
      continue
    if not print_match_guess_word(guess, wordOfTheDay):
      allowedGuesses -= 1
      continue
    if guess == wordOfTheDay:
      print(f"Congrats! You got the word right! {wordOfTheDay.capitalize()}")
      break


def print_rules():
  print(f"{CBOLD}LEGEND:{CEND}")
  print(f"{CITALIC}{CGREEN}\t you guessed right this letter!{CEND}")
  print(f"{CITALIC}{CYELLOW}\t you guessed right but in the wrong place...{CEND}")
  print(f"{CITALIC}{CGREY}\t letter not exists in the word.{CEND}")


class MatchTypes(Enum):
  NotExists = "Not exists"
  NotInPlace = "Not in the right place"
  Matched = "Guessed right"


# letters check
def print_match_guess_word(guess, word_of_the_day):
  valid = True
  print("-------------")
  guess_match_validations = try_match_guess(guess, word_of_the_day)
  for [guessed_letter, match_type] in guess_match_validations:
    if match_type == MatchTypes.Matched:
      print(f"{CBOLD}{CGREEN}{guessed_letter}{CEND} ", end="")
    elif match_type == MatchTypes.NotInPlace:
      print(f"{CBOLD}{CYELLOW}{guessed_letter}{CEND} ", end="")
      valid = False
    elif match_type == MatchTypes.NotExists:
      print(f"{CBOLD}{CGREY}{guessed_letter}{CEND} ", end="")
      valid = False
  print("\n-------------")
  return (valid,)


def try_match_guess(guess, word):
  return [
      [letter, try_match_letter(letter, word, index)]
      for index, letter in enumerate(guess)
  ]


def try_match_letter(guessed_letter, word, index):
  if guessed_letter == word[index]:
    return MatchTypes.Matched
  elif guessed_letter in word:
    return MatchTypes.NotInPlace
  else:  # guessed_letter not in word
    return MatchTypes.NotExists


# pick the word of the day: prints
def pick_word_of_the_day():
  allWordsByDate = dict()
  nowDateFormatted = datetime.now().strftime("%b %d %Y")
  wordlist_file = path.join(path.dirname(__file__), "./wordle_list.csv")
  with open(wordlist_file, newline="") as csvfile:
    wordlist = csv.reader(csvfile)
    for word in wordlist:
      allWordsByDate[word[0]] = word

  date, id, word = allWordsByDate[nowDateFormatted]
  print(f"{CBOLD}Word of the day: {date}, #{id}.{CEND}")
  return word


if __name__ == "__main__":
  wordle()
