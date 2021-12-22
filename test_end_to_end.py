import pytest
import date_interpreter

# Test case X


@pytest.mark.parametrize("file, expected",
                         [(['nofile'], 'Please provide valid path to a file\n'),
                          ])
def test_parametrized_file_input(capsys, file, expected):
    date_interpreter.main_function(['nofile'])
    output_print = capsys.readouterr()
    assert output_print.out == 'Please provide valid path to a file\n'


def test_invalid_file_input(capsys):
    date_interpreter.main_function(['nofile'])

    out, err = capsys.readouterr()
    assert out == 'Please provide valid path to a file\n'
    assert err == ''

# Test case X


def test_file_no_extension(capsys):
    date_interpreter.main_function([r'test_files\datefile_no_extension'])

    out, err = capsys.readouterr()
    assert out == 'Please provide valid path to a file\n'
    assert err == ''

# Test case X


def test_empty_file(capsys):
    date_interpreter.main_function([r'test_files\date_empty.txt'])

    out, err = capsys.readouterr()
    assert out == 'Please provide valid path to a file\n'
    assert err == ''

# Test case X


def test_valid_file_valid_dates(capsys):
    date_interpreter.main_function([r'test_files\datefile_valid_dates.txt'])

    out, err = capsys.readouterr()
    assert out == '0001-02-28\nThis year is leap: False. This month is 28 days long. This is the 59 day of the year\n0001-03-01\nThis year is leap: False. This month is 31 days long. This is the 60 day of the year\n'
    assert err == ''

# Test case X


def test_valid_file_invalid_dates(capsys):
    date_interpreter.main_function([r'test_files\datefile_invalid_dates.txt'])

    out, err = capsys.readouterr()
    assert out == '2021-77-77\nMonth has to be in range 1-12\n2021-02-29\nDay cannot be higher than maximum length of days in the month\n'
    assert err == ''

# Test case X


@pytest.mark.skip(reason="no way of currently testing this")
def test_big_zipped_file(capsys):
    date_interpreter.main_function([r'test_files\datefile_big.gz'])

    out, err = capsys.readouterr()
    assert out == 'Not yet coded error\n'
    assert err == ''

# Test case X


@pytest.mark.skip(reason="no way of currently testing this")
def test_big_file(capsys):
    date_interpreter.main_function([r'test_files\datefile_big.txt'])

    out, err = capsys.readouterr()
    assert out == 'Not yet coded error\n'
    assert err == ''