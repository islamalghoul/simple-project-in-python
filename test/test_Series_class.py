import pytest
from For_Series.Series_class import Series,Seriess

def test_get_title():
    Stranger_Things=Seriess("Stranger Things")
    Stranger_Things.get_data()
    actual=Stranger_Things.get_title()
    expected="Stranger Things"
    assert actual == expected
def test_get_overview():
    Stranger_Things=Seriess("Stranger Things")
    Stranger_Things.get_data()
    actual=Stranger_Things.get_overview()
    expected="When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces, and one strange little girl."
    assert actual == expected
def test_get_rating():
    Stranger_Things=Seriess("Stranger Things")
    Stranger_Things.get_data()
    actual=Stranger_Things.get_rating()
    expected=8.6
    assert actual == expected
def test_get_vote_count():
    Stranger_Things=Seriess("Stranger Things")
    Stranger_Things.get_data()
    actual=Stranger_Things.get_vote_count()
    expected=13985
    assert actual == expected
def test_get_date():
    Stranger_Things=Seriess("Stranger Things")
    Stranger_Things.get_data()
    actual=Stranger_Things.get_date()
    expected="2016-07-15"
    assert actual == expected