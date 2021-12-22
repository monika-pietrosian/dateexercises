import logging
import re
import argparse
from typing import Optional, Sequence

DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
MAX_MONTH = 12
MAX_YEAR = 9999
MIN_VALUE = 1


class Date:
    def __init__(self, year: int, month: int, day: int):

        self._year = self.is_valid_year(year)
        self._month = self.is_valid_month(month)
        self._day = self.is_valid_day(day)

    def is_valid_year(self, year):
        if year < MIN_VALUE or year > MAX_YEAR:
            raise ValueError("Year has to be in range 1-9999")
        return year

    def is_valid_month(self, month):
        if month < MIN_VALUE or month > MAX_MONTH:
            raise ValueError("Month has to be in range 1-12")
        return month

    def is_valid_day(self, day):
        if day < MIN_VALUE or day > self.month_length():
            raise ValueError("Day cannot be higher than maximum length of days in the month")
        return day

    def is_year_leap(self) -> bool:
        if self._year % 4 == 0 and self._year % 100 != 0 or self._year % 400 == 0:
            return True
        else:
            return False

    def month_length(self) -> int:
        if self._month == 2 and self.is_year_leap():
            return 29
        else:
            return DAYS_IN_MONTH[self._month - 1]

    def day_of_year(self) -> int:
        days_this_year = sum(DAYS_IN_MONTH[:self._month - 1]) + self._day
        if self._month > 2 and self.is_year_leap():
            days_this_year += 1
        return days_this_year


# Validate the data from the file

def read_file(file) -> str:
    with open(file) as file:
        lines = file.read()
    return lines


def find_all_occurencies(file_data: str) -> list:
    regex = r"""\d{4}-\d{2}-\d{2}"""
    dates_list = re.findall(regex, file_data)
    return dates_list


def validated_date_in_input(user_data: str) -> tuple:
    try:
        date_list = user_data.split('-', )
        Date1 = Date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        return True, Date1
    except Exception as exception:
        return False, exception


# Print the result to the user.

def print_results(Date1: Date):
    logging.info(
        f'This year is leap: {Date1.is_year_leap()}. This month is {Date1.month_length()} days long. This is the {Date1.day_of_year()} day of the year')


# You enter the date as the first argument from the console

def main_function(argv: Optional[Sequence[str]] = None) -> int:
    level = logging.INFO
    fmt = '%(message)s'
    logging.basicConfig(level=level, format = fmt, handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()])
    parser = argparse.ArgumentParser()
    parser.add_argument('user_file')
    args = parser.parse_args(argv)
    try:
        file_data = str(args.user_file)
        dates_list = read_file(file_data)

        for date in find_all_occurencies(dates_list):
            validation_tuple = validated_date_in_input(date)
            is_valid, validation_output = validation_tuple  # Is the date valid? True or False
            # Returns valid date or the reason it isn't valid
            logging.info(date)

            if is_valid is False:
                logging.info(validation_output)
            else:
                print_results(validation_output)

    except Exception as exception:
        logging.info('Please provide valid path to a file')
        return 1


if __name__ == '__main__':
    main_function()
