import pytest
import date_interpreter

# TC-15

@pytest.mark.parametrize("string, expected", [
    (
            '''python date_interpreter.py 0004-03-01 python date_interpreter.py 2021-02-28 python date_interpreter.py 
    2021/01/01''',
            ['0004-03-01', '2021-02-28']),
])
def test_finding_all_occurencies(string, expected):
    func_result = date_interpreter.find_all_occurencies(string)
    assert func_result == expected

# TC-16


@pytest.mark.parametrize("file, expected", [
    (r'test_files\datefile_invalid_dates.txt',
     'python date_interpreter.py 2021-77-77\npython date_interpreter.py 2021-02-29'),
])
def test_reading_file(file, expected):
    func_result = date_interpreter.read_file(file)
    assert func_result == expected

# TC-17


@pytest.mark.parametrize("string, expected", [
    ('2021-77-77', False,),
    ('2021-02-12', True,),
])
def test_validate_input(string, expected):
    validation_tuple = date_interpreter.validated_date_in_input(string)
    is_valid, validation_output = validation_tuple
    assert is_valid == expected
    if is_valid is True:
        assert isinstance == (validation_output, date_interpreter.Date)
    else:
        assert isinstance == (validation_output, ValueError)

# TC-18


def test_printing_results(capsys):
    Date1 = date_interpreter.Date(1, 2, 28)  # 0001-02-28
    date_interpreter.print_results(Date1)
    out, err = capsys.readouterr()
    assert out == 'This year is leap: False. This month is 28 days long. This is the 59 day of the year\n'
    assert err == ''
