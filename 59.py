import operator
from functools import partial
from itertools import (chain,
                       zip_longest,
                       product)
from string import printable
from typing import (Iterable,
                    Container,
                    Sequence)

from utils import english_text


def decrypt(*,
            codes: Sequence[int],
            password: Sequence[int]) -> Iterable[int]:
    password_length = len(password)
    codes_parts = [codes[offset::password_length]
                   for offset in range(password_length)]
    decrypted_codes_parts = [map(partial(operator.xor,
                                         character),
                                 codes_part)
                             for codes_part, character in zip(codes_parts,
                                                              password)]
    decrypted_codes = zip_longest(*decrypted_codes_parts)
    yield from filter(None, chain.from_iterable(decrypted_codes))


def guess_password(*,
                   codes: Sequence[int],
                   password_domain: Iterable[int],
                   password_length: int,
                   text_characters: Container[str]
                   ) -> Sequence[int]:
    for password in valid_passwords(codes=codes,
                                    password_domain=password_domain,
                                    password_length=password_length,
                                    text_characters=text_characters):
        decrypted_codes = decrypt(codes=codes,
                                  password=password)
        decrypted_text = ''.join(map(chr, decrypted_codes))
        if english_text(decrypted_text):
            yield password


def valid_passwords(*,
                    codes: Sequence[int],
                    password_domain: Iterable[int],
                    password_length: int,
                    text_characters: Container[str]
                    ) -> Iterable[Sequence[int]]:
    codes_parts = [codes[offset::password_length]
                   for offset in range(password_length)]
    valid_passwords_codes = [
        [password_code
         for password_code in password_domain
         if all(chr(code ^ password_code) in text_characters
                for code in codes_part)]
        for codes_part in codes_parts]
    yield from product(*valid_passwords_codes)


def xor_decryption(*,
                   codes: Sequence[int],
                   password_domain: Iterable[int],
                   password_length: int,
                   text_characters: Container[str] = printable
                   ) -> Iterable[int]:
    password, = guess_password(codes=codes,
                               password_domain=password_domain,
                               password_length=password_length,
                               text_characters=text_characters)
    yield from decrypt(codes=codes,
                       password=password)


with open('cipher.txt') as text_codes_file:
    text_codes_str = text_codes_file.read()
text_codes = list(map(int, text_codes_str.split(',')))
lower_case_characters_codes = range(ord('a'), ord('z') + 1)
decrypted_text_codes = xor_decryption(
    codes=text_codes,
    password_domain=lower_case_characters_codes,
    password_length=3)

assert sum(decrypted_text_codes) == 107_359
