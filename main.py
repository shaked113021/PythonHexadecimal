A_in_ascii = 65


def convertDigitToHex1(num: int) -> str:
    if num < 0 or num > 15:
        raise Exception(f'input must be between 0 to 15, given input {num}')
    elif num <= 9:
        return f'{num}'
    else:
        offset = 10 - num
        return f'{chr(A_in_ascii + offset)}'


def convertDigitToHex2(num: int) -> str:
    if num < 0 or num > 15:
        raise Exception(f'input must be between 0 to 15, given input {num}')
    elif num <= 9:
        return f'{num}'
    elif num == 10:
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'


def regularAlgorithm(num: int) -> str:
    pass


def moduloAlgorithm(num: int) -> str:
    pass

