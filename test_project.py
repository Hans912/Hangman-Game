from project import check_word
from project import check_letter
from project import mistake

def test_check_word():
    assert check_word("hans", "h") == True
    assert check_word("hans", "f") == False

def test_check_letter():
    assert check_letter("hans", "h", [' - ', ' - ', ' - ', ' - ']) == ['h', ' - ', ' - ', ' - ']
    assert check_letter("hans", "a", [' - ', ' - ', ' - ', ' - ']) == [' - ', 'a', ' - ', ' - ']

def test_mistake():
    assert mistake(0) == print("---") 
