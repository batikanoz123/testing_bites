from lib.gratitudes import *

def test_adds_gratitude():
    gratitude1 = Gratitudes()
    result = gratitude1.add("Food")
    assert result == ["Food"]

def test_format():
    gratitude1 = Gratitudes()
    gratitude1.add("Food")
    result = gratitude1.format()
    assert result == "Be grateful for : Food"
