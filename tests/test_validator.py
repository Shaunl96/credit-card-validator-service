from src.validator import is_valid_credit_card

def test_valid_cards():
    assert is_valid_credit_card("49927398716")
    assert is_valid_credit_card("1234567812345670")
    assert is_valid_credit_card("2222405343248877")
    assert is_valid_credit_card("2222990905257051")

def test_invalid_cards():
    assert not is_valid_credit_card("49927398717")
    assert not is_valid_credit_card("1234567812345678")
