roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def handleNumerals(numerals):
    return {"I": handleStartsWithI(numerals),
            "V": handleStartsWithV(numerals),
            "X": handleStartsWithX(numerals),
            "L": handleStartsWithL(numerals),
            "C": handleStartsWithC(numerals),
            "D": handleStartsWithD(numerals),
            "M": handleStartsWithM(numerals),
            }[numerals[0]]


def handleStartsWithV(numerals):
    result = 0
    if len(numerals) == 1:
        return roman_numerals[numerals]
    for numeral in numerals:
        result += roman_numerals[numeral]
    return result


def handleStartsWithI(numerals):
    if len(set(numerals)) == 1:
        return len(numerals)
    return roman_numerals[numerals[1]] - 1


def handleStartsWithX(numerals):
    result = 0
    if len(set(numerals)) == 1:
        return len(numerals) * 10
    elif len(numerals) == 2:
        return roman_numerals[numerals[1]] - 10
    else:
        result += 10 + handleNumerals(numerals[1:])
    return result


def handleStartsWithL(numerals):
    pass


def handleStartsWithC(numerals):
    pass


def handleStartsWithD(numerals):
    pass


def handleStartsWithM(numerals):
    pass


print(handleNumerals("XL"))
