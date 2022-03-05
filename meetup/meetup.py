"""
    Meetup exercise
"""

from datetime import date, timedelta
from calendar import monthrange

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def meetup(year, month, week, day_of_week):
    """
        Return the actual date
    """
    weekday_dct = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }
    week_dct = {
        "1st": 1,
        "2nd": 2,
        "3rd": 3,
        "4th": 4,
        "5th": 5
    }
    try:
        week_delta = timedelta(weeks=1)
        actual_date = date(year, month, 1)
        while actual_date.weekday() != weekday_dct[day_of_week]:
            actual_date += timedelta(days=1)
        if week == "teenth":
            while actual_date.day < 13:
                actual_date += week_delta
        elif week == "last":
            while actual_date.day + 7 <= monthrange(actual_date.year, actual_date.month)[1]:
                actual_date += week_delta
        else:
            time, old_month = 1, actual_date.month
            while time < week_dct[week]:
                actual_date += week_delta
                time += 1
            if actual_date.month != old_month:
                raise MeetupDayException("That day does not exist.")
        return actual_date
    except ValueError:
        raise MeetupDayException("That day does not exist.")
