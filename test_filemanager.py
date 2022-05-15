from victory import *


def test_date_to_str():
    assert date_to_str("01.01.2020") == "первое января 2020 года"


from main import *


def test_separator():
    assert len(separator(30)) == 30
    assert separator(30) == ("*" * 30)
    for element in separator():
        assert element == "*"


def test_is_correct_choice():
    assert is_correct_choice("8") == False


from filemanager import *
def test_filenames():
    assert "menu.py", "bill.py" in filenames()

def test_author_info():
    assert author_info() == 'Leonid Orlov'


import filecmp
def test_copy_file_or_folder():
    assert filecmp.cmp("copy_bill.py", "bill.py") == True
