def is_valid_credit_card(card_number: str) -> bool:
    total = 0
    length = len(card_number)
    parity = length % 2

    for i in range(length - 1, -1, -1):
        digit = int(card_number[i])

        if (i + 1) % 2 == parity:
            total += digit
        else:
            doubled = digit * 2
            total += doubled - 9 if doubled > 9 else doubled

    return total % 10 == 0