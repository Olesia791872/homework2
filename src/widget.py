from masks import get_mask_account, get_mask_card_number


def masc_account_card(type_and_number: str) -> str:
    """Account/card masking function"""
    text_result = " "
    digit_result = " "
    digit_count = 0
    for symbol in type_and_number:
        if symbol.isalpha():
            text_result += symbol
        elif symbol.isdigit():
            digit_count += 1
            digit_result += symbol
    if digit_count > 16:
        return f"{text_result} {get_mask_account(digit_result)}"
    else:
        return f"{text_result} {get_mask_card_number(digit_result)}"


print(masc_account_card("check 35383033474447895560"))


def get_date(get_str: str) -> str:
    """The function takes a string and returns a date in the format DD.MM.YYYY"""
    date_slise = get_str[0:10].split("_")
    return ".".join(date_slise[::-1])
