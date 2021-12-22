import pytest
import date_interpreter


# @py.test.mark.smoke
# pytestmark = [pytest.mark.smoke, py.test.mark.functional]
# py.test smoke
@pytest.fixture
def create_class() -> date_interpreter.Date:
    Date1 = date_interpreter.Date(year, month, day)
    pass

@pytest.mark.parametrize("year,month,day,expected",
                         [(4, 3, 1, 61),
                          (3, 3, 1, 60),
                          (4, 12, 31, 366),
                          (3, 12, 31, 365),
                          (1, 1, 1, 1),
                          (2000, 1, 1, 1),
                          ])
def test_day_of_year(year, month, day, expected):
    Date1 = date_interpreter.Date(year, month, day)
    assert Date1.day_of_year() == expected


@pytest.mark.parametrize("year,month,day,expected",
                         [(2000, 1, 0, 'ValueError: Day cannot be higher than maximum length of days in the month'),
                          (2000, 1, 32, 'ValueError: Day cannot be higher than maximum length of days in the month'),
                          ])
def test_day_of_year_error(year, month, day, expected):
    with pytest.raises(Exception) as e_info:
        Date1 = date_interpreter.Date(year, month, day)
        assert Date1.day_of_year() == expected


@pytest.mark.parametrize("year,month,day,expected",
                         [(2100, 2, 1, False),
                          (1700, 2, 28, False),
                          (1, 3, 1, False),
                          (9999, 1, 1, False),
                          (1600, 12, 2, True),
                          (2000, 12, 30, True),
                          ])
def test_is_year_leap(year, month, day, expected):
    Date1 = date_interpreter.Date(year, month, day)
    assert Date1.is_year_leap() == expected


@pytest.mark.parametrize("year,month,day,expected",
                         [(0, 12, 30, 'ValueError: Year has to be in range 1-9999'),
                          (10000, 12, 30, 'ValueError: Year has to be in range 1-9999'),
                          ])
def test_is_year_leap_error(year, month, day, expected):
    with pytest.raises(Exception) as e_info:
        Date1 = date_interpreter.Date(year, month, day)
        assert Date1.is_year_leap() == expected


@pytest.mark.parametrize("year,month,day,expected",
                         [(1, 2, 28, 28),
                          (29, 2, 3, 28),
                          (4, 12, 1, 31),
                          ])
def test_month_length(year, month, day, expected):
    Date1 = date_interpreter.Date(year, month, day)
    assert Date1.month_length() == expected


@pytest.mark.parametrize("year,month,day,expected",
                          [(4, 0, 1, 'ValueError: Year has to be in range 1-12'),
                          (4, 13, 1, 'ValueError: Year has to be in range 1-12'),
                          ])
def test_month_length_error(year, month, day, expected):
    with pytest.raises(Exception) as e_info:
        Date1 = date_interpreter.Date(year, month, day)
        assert Date1.month_length() == expected
