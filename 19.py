from datetime import date
from itertools import product

weekdays = ['Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday']


def weekdays_count(*,
                   year_start: int,
                   year_stop: int,
                   year_step: int = 1,
                   target_weekday: str) -> int:
    target_weekday = weekdays.index(target_weekday)
    months_indexes = range(1, 13)
    years_indexes = range(year_start, year_stop, year_step)
    first_months_days = (date(year=year_index,
                              month=month_index,
                              day=1)
                         for month_index, year_index in product(months_indexes,
                                                                years_indexes))
    first_months_days_weekdays = map(date.weekday,
                                     first_months_days)

    def is_target_weekday(weekday: int) -> bool:
        return weekday == target_weekday

    return sum(1 for _ in filter(is_target_weekday,
                                 first_months_days_weekdays))


assert weekdays_count(year_start=1901,
                      year_stop=2001,
                      target_weekday='Sunday') == 171
