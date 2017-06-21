from string import ascii_uppercase

from utils import (parse_lines,
                   triangular,
                   capacity)

letters_positions = {letter: position
                     for position, letter in enumerate(ascii_uppercase,
                                                       start=1)}


def triangular_word(word: str) -> bool:
    word_value = sum(letters_positions[letter]
                     for letter in word)
    return triangular(word_value)


with open('words.txt') as words_file:
    words = list(parse_lines(words_file))

triangular_words = filter(triangular_word, words)

assert triangular_word('SKY')
assert capacity(triangular_words) == 162
