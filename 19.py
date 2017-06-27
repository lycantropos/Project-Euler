from datetime import date
from itertools import product
from typing import Iterable

from utils import capacity

weekdays = ['Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday']


def weekdays_count(*,
                   years: Iterable[int],
                   target_weekday: str) -> int:
    target_weekday = weekdays.index(target_weekday)
    months = range(1, 13)
    first_months_days = (date(year=year,
                              month=month,
                              day=1)
                         for month, year in product(months, years))
    first_months_days_weekdays = map(date.weekday,
                                     first_months_days)

    def is_target_weekday(weekday: int) -> bool:
        return weekday == target_weekday

    return capacity(filter(is_target_weekday,
                           first_months_days_weekdays))


assert weekdays_count(years=range(1901, 2001),
                      target_weekday='Sunday') == 171
