from src.wordle import MatchTypes, print_match_guess_word, try_match_guess, try_match_letter
import pytest

word_of_the_day = "HAPPY"


def test_correct_matched():
  match_type = try_match_letter("P", word_of_the_day, 2)
  assert match_type == MatchTypes.Matched


def test_notinplace_matched():
  match_type = try_match_letter("P", word_of_the_day, 0)
  assert match_type == MatchTypes.NotInPlace


def test_notexists_letter():
  match_type = try_match_letter("I", word_of_the_day, 0)
  assert match_type == MatchTypes.NotExists


def test_double_letter_notinplace_matched():
  match_types = try_match_guess("PPIPE", word_of_the_day)
  print_match_guess_word("PPIPE", word_of_the_day)
  assert match_types[0][1] == MatchTypes.NotInPlace
  assert match_types[1][1] == MatchTypes.NotExists
  assert match_types[3][1] == MatchTypes.Matched


def test_double_letter_both_notinplace():
  match_types = try_match_guess("PPIVE", word_of_the_day)
  print_match_guess_word("PPIVE", word_of_the_day)
  assert match_types[0][1] == MatchTypes.NotInPlace
  assert match_types[1][1] == MatchTypes.NotInPlace


def test_double_letter_marked_one():
  match_types = try_match_guess("PIVEV", word_of_the_day)
  print_match_guess_word("PIVEV", word_of_the_day)
  assert match_types[0][1] == MatchTypes.NotInPlace
  assert match_types[1][1] == MatchTypes.NotExists
