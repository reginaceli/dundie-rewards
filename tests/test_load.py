from dundie.core import load


def test_load():
    """Test load function"""
    assert len(load("tests/assets/people.csv")) == 2
    assert load("tests/assets/people.csv")[0][0] == "J"
