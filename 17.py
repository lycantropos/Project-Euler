from typing import Iterable

DIGITS_NAMES = {0: 'zero',
                1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine'}
NUMBERS_NAMES = {10: 'ten',
                 11: 'eleven',
                 12: 'twelve',
                 13: 'thirteen',
                 14: 'fourteen',
                 15: 'fifteen',
                 16: 'sixteen',
                 17: 'seventeen',
                 18: 'eighteen',
                 19: 'nineteen',
                 20: 'twenty',
                 30: 'thirty',
                 40: 'forty',
                 50: 'fifty',
                 60: 'sixty',
                 70: 'seventy',
                 80: 'eighty',
                 90: 'ninety',
                 1_000: 'one thousand'}
NUMBERS_NAMES.update({number * 100: DIGITS_NAMES[number] + ' hundred'
                      for number in range(1, 10)})


def number_to_words(number: int) -> Iterable[str]:
    try:
        yield from NUMBERS_NAMES[number].split()
    except KeyError:
        hundreds = (number // 100) * 100
        dozens = number % 100
        try:
            yield from NUMBERS_NAMES[hundreds].split()
            if dozens:
                yield 'and'
        except KeyError:
            # no hundreds
            pass
        try:
            yield NUMBERS_NAMES[dozens]
        except KeyError:
            digit = dozens % 10
            dozens -= digit
            try:
                yield NUMBERS_NAMES[dozens]
            except KeyError:
                # no dozens
                pass
            yield DIGITS_NAMES[digit]


def numbers_to_words(*,
                     start: int = 1,
                     stop: int,
                     step: int = 1,
                     sep: str = ' ') -> Iterable[str]:
    numbers = range(start, stop, step)
    for number in numbers:
        yield sep.join(number_to_words(number))


def numbers_letters_count(*,
                          start: int = 1,
                          stop: int,
                          step: int = 1) -> int:
    return letters_count(numbers_to_words(start=start,
                                          stop=stop,
                                          step=step,
                                          sep=''))


def letters_count(words: Iterable[str]) -> int:
    return sum(map(len, words))


assert letters_count(number_to_words(342)) == 23
assert letters_count(number_to_words(115)) == 20

assert numbers_letters_count(stop=6) == 19
assert numbers_letters_count(stop=1001) == 21_124
