def roman_to_integer(roman_numeral):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    integer_value = 0
    prev_value = 0

    for numeral in reversed(roman_numeral):
        value = roman_dict[numeral]
        if value >= prev_value:
            integer_value += value
        else:
            integer_value -= value
        prev_value = value

    return integer_value

if __name__ == "__main__":
    # Example usage
    roman_numeral = "XIV"
    integer_value = roman_to_integer(roman_numeral)
    print(f"The integer value of {roman_numeral} is: {integer_value}")
