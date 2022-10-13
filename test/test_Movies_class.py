import pytest
from For_Movies.Movies_class import Movie,Movies

def test_get_title():
    spider_man=Movies("spiderman")
    spider_man.get_data()
    actual=spider_man.get_title()
    expected="Spider-Man"
    assert actual == expected
def test_get_overview():
    spider_man=Movies("spiderman")
    spider_man.get_data()
    actual=spider_man.get_overview()
    expected="After being bitten by a genetically altered spider at Oscorp, nerdy but endearing high school student Peter Parker is endowed with amazing powers to become the superhero known as Spider-Man."
    assert actual == expected
def test_get_rating():
    spider_man=Movies("spiderman")
    spider_man.get_data()
    actual=spider_man.get_rating()
    expected=7.3
    assert actual == expected
def test_get_vote_count():
    spider_man=Movies("spiderman")
    spider_man.get_data()
    actual=spider_man.get_vote_count()
    expected=16265
    assert actual == expected
def test_get_date():
    spider_man=Movies("spiderman")
    spider_man.get_data()
    actual=spider_man.get_date()
    expected="2002-05-01"
    assert actual == expected

