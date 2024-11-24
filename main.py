def main():

    num1 = str(input("Введите первое число: "))
    num2 = str(input("Введите второе число: "))

    de = hex_add(num1, num2)
    print(de)


def DecimalToBin(num):
    if num == 0:
        return "0"

    bin_number = ""
    is_negative = num < 0
    decimal_number = abs(num)

    while decimal_number > 0:
        remainder = decimal_number % 2
        bin_number = str(remainder) + bin_number
        decimal_number //= 2

    if is_negative:
        bin_number = "-" + bin_number

    return bin_number

def DecimalToOct(num):
    if num == 0:
        return "0"

    octal_number = ""
    is_negative = num < 0
    decimal_number = abs(num)

    while decimal_number > 0:
        remainder = decimal_number % 8
        octal_number = str(remainder) + octal_number
        decimal_number //= 8

    if is_negative:
        octal_number = "-" + octal_number

    return octal_number
def DecimalToHex(num):
    if num == 0:
        return "0"

    hex_characters = "0123456789ABCDEF"
    hexadecimal_number = ""
    is_negative = num < 0
    decimal_number = abs(num)

    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_number = hex_characters[remainder] + hexadecimal_number
        decimal_number //= 16

    if is_negative:
        hexadecimal_number = "-" + hexadecimal_number

    return hexadecimal_number


def BinaryToDec(num):
    decimal_number = 0
    st = 0

    # Работаем с числом как со строкой для обработки каждого символа
    for n in reversed(str(num)):  # Перебор от младших разрядов
        if n not in "01":
            raise ValueError("Это не двоичное число.")
        decimal_number += int(n) * (2 ** st)
        st += 1

    return decimal_number

def BinaryToOct(num):

    num = str(num)
    # Проверяем, что введено корректное двоичное число
    if not all(digit in "01" for digit in num):
        raise ValueError("Это не двоичное число.")

    # Дополняем двоичное число нулями слева для кратности трем
    while len(num) % 3 != 0:
        num = "0" + num

    # Разбиваем число на триады
    triads = [num[i:i + 3] for i in range(0, len(num), 3)]

    # Переводим каждую триаду в восьмеричное представление
    octal_number = ""
    for triad in triads:
        decimal_value = BinaryToDec(triad)  # Перевод триады из двоичной в десятичную
        octal_number += str(decimal_value)

    return octal_number

def BinaryToHex(num):
    hex_characters = "0123456789ABCDEF"
    num = str(num)
    # Проверяем, что введено корректное двоичное число
    if not all(digit in "01" for digit in num):
        raise ValueError("Это не двоичное число.")

    # Дополняем двоичное число нулями слева для кратности трем
    while len(num) % 4 != 0:
        num = "0" + num

    # Разбиваем число на триады
    triads = [num[i:i + 4] for i in range(0, len(num), 4)]

    # Переводим каждую триаду в восьмеричное представление
    octal_number = ""
    for triad in triads:
        decimal_value = hex_characters[BinaryToDec(triad)]  # Перевод триады из двоичной в десятичную
        octal_number += str(decimal_value)

    return octal_number


def OctalToBin(num):
    num = str(num)
    path = [num[i:i + 1] for i in range(0, len(num), 1)]

    binary_number = ""
    for i in path:
        binary = str(DecimalToBin(int(i)))
        while len(binary) % 3 != 0:
            binary = "0" + binary
        binary_number += binary

    return int(binary_number)
def OctalToDec(num):
    num = str(num)
    path = [num[i:i + 1] for i in range(0, len(num), 1)]

    binary_number = 0
    j = 1
    for i in path:
        binary = int(i) * 8**(len(path)-j)
        binary_number = binary_number + binary
        j = j + 1

    return int(binary_number)

def OctalToHex(num):
    dec = int(OctalToDec(num))
    oct = DecimalToHex(dec)
    return oct


def HexToBin(num):
    hex_characters = "0123456789ABCDEF"
    num = str(num)
    path = [num[i:i + 1] for i in range(0, len(num), 1)]

    binary_number = ""
    for i in path:
        binary = str(DecimalToBin(int(hex_characters.index(i))))
        while len(binary) % 4 != 0:
            binary = "0" + binary
        binary_number += binary

    return int(binary_number)

def HexToDec(num):
    hex_characters = "0123456789ABCDEF"
    num = str(num)
    path = [num[i:i + 1] for i in range(0, len(num), 1)]

    binary_number = 0
    j = 1
    for i in path:
        binary = hex_characters.index(i) * 16**(len(path)-j)
        binary_number = binary_number + binary
        j = j + 1

    return int(binary_number)


def binary_addition(n1, n2):
    max_len = max(len(n1), len(n2))
    bin1 = n1.zfill(max_len)  # Дополняем нулями слева для одинаковой длины
    bin2 = n2.zfill(max_len)

    carry = 0
    result = ""

    # Идем от младших разрядов к старшим
    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        sum_bits = bit1 + bit2 + carry
        result = str(sum_bits % 2) + result  # Остаток от деления на 2
        carry = sum_bits // 2  # Целая часть от деления на 2

    if carry:
        result = "1" + result

    return result

def binary_subtraction_manual(bin1, bin2):
    is_negative = ""
    if bin1 < bin2:
        bin3 = bin1
        bin1 = bin2
        bin2 = bin3
        is_negative = "-"

    # Дополняем нулями для одинаковой длины
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    result = ""
    borrow = 0

    # Проходим по разрядам справа налево
    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin1[i]) + borrow
        bit2 = int(bin2[i])

        if bit1 < bit2:
            # Заимствуем единицу из старшего разряда
            borrow = -1
            bit1 += 2
        else:
            borrow = 0

        result = str(bit1 - bit2) + result

    # Удаляем ведущие нули
    return is_negative + result.lstrip("0") or "0"


def octal_addition(n1, n2):
    max_len = max(len(n1), len(n2))
    bin1 = n1.zfill(max_len)  # Дополняем нулями слева для одинаковой длины
    bin2 = n2.zfill(max_len)

    carry = 0
    result = ""

    # Идем от младших разрядов к старшим
    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        sum_bits = bit1 + bit2 + carry
        carry = 0
        if sum_bits > 7:
            sum_bits = sum_bits - 8
            carry = 1
        result = str(sum_bits) + result  # Остаток от деления на 2


    if carry:
        result = "1" + result

    return result

def octal_sub(bin1, bin2):
    is_negative = ""
    if int(bin1) < int(bin2):
        bin3 = bin1
        bin1 = bin2
        bin2 = bin3
        is_negative = "-"

    return is_negative + str(int(bin1) - int(bin2)) or "0"


def hex_add(n1, n2):
    hex_characters = "0123456789ABCDEF"
    max_len = max(len(n1), len(n2))
    bin1 = n1.zfill(max_len)  # Дополняем нулями слева для одинаковой длины
    bin2 = n2.zfill(max_len)

    borrow = 0
    result = ""

    # Идем от младших разрядов к старшим
    for i in range(max_len - 1, -1, -1):
        bit1 = hex_characters.index(bin1[i]) + borrow
        bit2 = hex_characters.index(bin2[i])
        if bit1 < bit2:
            # Заимствуем единицу из старшего разряда
            borrow = -1
            bit1 += 16
        else:
            borrow = 0

        result = str(hex_characters[bit1-bit2]) + result  # Остаток от деления на 2

    if borrow == -1:
        result = "-F" + result

    return result

def hex_sub(bin1, bin2):
    hex_characters = "0123456789ABCDEF"
    # Дополняем нулями для одинаковой длины
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    result = ""
    borrow = 0

    # Проходим по разрядам справа налево
    for i in range(max_len - 1, -1, -1):
        bit1 = hex_characters.index(bin1[i]) + borrow
        bit2 = hex_characters.index(bin2[i])

        if bit1 < bit2:
            # Заимствуем единицу из старшего разряда
            borrow = -1
            bit1 += 16
        else:
            borrow = 0

        result = str(hex_characters[bit1 - bit2]) + result

    # Удаляем ведущие нули
    return result.lstrip("0") or "0"


if __name__ == "__main__":
	main()