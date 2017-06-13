from typing import (Iterable,
                    Iterator)

COINS = {
    '1p': 1,
    '2p': 2,
    '5p': 5,
    '10p': 10,
    '20p': 20,
    '50p': 50,
    '£1': 100,
    '£2': 200
}


def is_coins_sum(value: int,
                 *,
                 coins: Iterator[int]):
    coin = next(coins)
    rest_coins = list(coins)
    if not rest_coins:
        yield value - (value // coin) * coin == 0
    else:
        for coins_count in range(value // coin + 1):
            balance = value - coin * coins_count
            if balance == 0:
                yield True
            elif balance > 0:
                yield from is_coins_sum(balance,
                                        coins=iter(rest_coins))
            else:
                break


def coin_sums(value: int,
              coins: Iterable[int]) -> int:
    return sum(is_coins_sum(value,
                            coins=iter(sorted(coins,
                                              reverse=True))))


assert coin_sums(200, coins=COINS.values()) == 73_682
