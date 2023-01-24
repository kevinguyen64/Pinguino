from project import guess, gender, birthdate, genre, grammys
import pytest


def test_correct_guess():
    with pytest.raises(SystemExit):
        guess("Prince", "Prince")
    with pytest.raises(SystemExit):
        guess("Carrie Underwood", "Carrie Underwood")


def test_wrong_guess():
    assert guess("Prince", "Mariah Carey") == f"\nSorry! Pinguino is not Prince. Here's another hint..."
    assert guess("Katy Perry", "Elton John") == f"\nSorry! Pinguino is not Katy Perry. Here's another hint..."

def test_gender():
    assert gender("Prince") == "Male"
    assert gender("Mariah Carey") == "Female"


def test_birthdate():
    assert birthdate("Prince") == "06/07/1958"
    assert birthdate("Mariah Carey") == "03/27/1969"


def test_genre():
    assert genre("Luke Bryan") == "Country"
    assert genre("Whitney Houston") == "R&B"


def test_grammys():
    assert grammys("Alicia Keys") == "15"
    assert grammys("Elton John") == "6"