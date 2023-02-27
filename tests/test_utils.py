import pytest
from dundie.utils.email import check_valid_email


@pytest.mark.unit
@pytest.mark.parametrize(
    "address",
    ["catas@gmail.com", "joe@doe.com", "a@b.pt"]
)
def test_positive_check_valid_email(address):
    """Should be check if email is valid"""
    assert check_valid_email(address) is True


@pytest.mark.unit
@pytest.mark.parametrize(
    "address",
    ["catas@.com", "@doe.com", "a@b"]
)
def test_negative_check_invalid_email(address):
    """Should be check if email is valid"""
    assert check_valid_email(address) is False