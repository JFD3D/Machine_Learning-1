"""utlitiez"""
import datetime


class TimeHandler(object):
    """wuuut"""
    def __init__(self, start_date):
        self.start_date = str_to_date(start_date)

    def date_to_days(self, date):
        """erh"""
        date = str_to_date(date)
        return (date-self.start_date).days


def clean_text(text):
    """cleans a string for nasties"""
    return text.replace('\n', '').replace('"', '')


def get_ymd(date):
    """transforms date to a int"""
    date = date.split()[0]
    return [int(x) for x in date.split('-')]


def str_to_date(date):
    """str to date"""
    datel = get_ymd(date)
    return datetime.date(datel[0], datel[1], datel[2])


def flatten_2d(lst):
    """lst[][] ==> lst[]"""
    return [item for sublist in lst for item in sublist]
