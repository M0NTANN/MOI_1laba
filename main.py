def main():
    while True:
        print("\n\n\nВыберите действие: \n"
              "1 Конвертация \n"
              "2 Сложение \n"
              "3 Вычистание \n"
              "4 Выход")
        choiceU = int(input(">>>"))

        if choiceU == 1:
            print("Выберите перевод из какой системы счисления в какую нужен:\n"
                  "1 Из 2cc в 8cc\n"
                  "2 Из 2cc в 10cc\n"
                  "3 Из 2cc в 16ccя\n"
                  
                  "4 Из 8cc в 2cc\n"
                  "5 Из 8cc в 10cc\n"
                  "6 Из 8cc в 16cc\n"
                  
                  "7 Из 10cc в 2cc\n"
                  "8 Из 10cc в 8cc\n"
                  "9 Из 10cc в 16cc\n"

                  "10 Из 16cc в 2cc\n"
                  "11 Из 16cc в 10cc\n"
                  )
            choiceSS = int(input(">>"))

            if choiceSS == 1:
                num1 = input("Введите первое число \n")

                print("Ответ: " + BinaryToOct(num1))

            elif choiceSS == 2:
                num1 = int(input("Введите первое число\n"))
                print("Ответ: " + str(BinaryToDec(num1)))

            elif choiceSS == 3:
                num1 = input("Введите первое число\n")
                print("Ответ: " + BinaryToHex(num1))

            elif choiceSS == 4:
                num1 = input("Введите первое число\n")
                print("Ответ: " + str(OctalToBin(num1)))

            elif choiceSS == 5:
                num1 = input("Введите первое число\n")
                print("Ответ: " + str(OctalToDec(num1)))

            elif choiceSS == 6:
                num1 = input("Введите первое число \n")
                print("Ответ: " + OctalToHex(num1))

            elif choiceSS == 7:
                num1 = input("Введите первое число\n")
                print("Ответ: " + DecimalToBin(num1))

            elif choiceSS == 8:
                num1 = input("Введите первое число\n")
                print("Ответ: " + DecimalToOct(num1))

            elif choiceSS == 9:
                num1 = input("Введите первое число\n")
                print("Ответ: " + DecimalToHex(num1))

            elif choiceSS == 10:
                num1 = input("Введите первое число\n")
                print("Ответ: " + str(HexToBin(num1)))

            elif choiceSS == 11:
                num1 = input("Введите первое число\n")
                print("Ответ: " + str(HexToDec(num1)))

        elif choiceU == 2:
            print("Выберите в какой системе счисления складывавем:\n"
                  "1 В 2cc\n"
                  "2 В 8cc\n"
                  "3 В 16cc\n")
            choiceAdd = int(input(">>>"))

            if choiceAdd == 1:
                num1 = input("Введите первое число \n")
                num2 = input("Введите второе число\n")
                print("Ответ: " + BinaryAdd(num1, num2))

            elif choiceAdd == 2:
                num1 = input("Введите первое число \n")
                num2 = input("Введите второе число\n")
                print("Ответ: " + OctalAdd(num1, num2))

            elif choiceAdd == 3:
                num1 = input("Введите первое число \n")
                num2 = input("Введите второе число\n")
                print("Ответ: " + HexAdd(num1, num2))

        elif choiceU == 3:
            print("Выберите в какой системе счисления вычитаем:\n"
                  "1 В 2cc\n"
                  "2 В 8cc\n"
                  "3 В 16cc\n")
            choiceSub = int(input(">>>"))

            if choiceSub == 1:
                num1 = input("Введите первое число \n")
                num2 = input("Введите второе число\n")
                print("Ответ: " + BinarySub(num1, num2))

            elif choiceSub == 2:
                num1 = input("Введите первое число \n")
                num2 = input("Введите второе число\n")
                print("Ответ: " + OctalSub(num1, num2))

            elif choiceSub == 3:
                num1 = input("Введите первое число \n")
                num2 = input("Введите второе число\n")
                print("Ответ: " + HexSub(num1, num2))

        elif choiceU == 4:
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


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


def BinaryAdd(num1, num2):
    max_len = max(len(num1), len(num2))
    bin1 = num1.zfill(max_len)  # Дополняем нулями слева для одинаковой длины
    bin2 = num2.zfill(max_len)

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
def BinarySub(num1, num2):
    is_negative = ""
    if num1 < num2:
        num3 = num1
        num1 = num2
        num2 = num3
        is_negative = "-"

    # Дополняем нулями для одинаковой длины
    max_len = max(len(num1), len(num2))
    bin1 = num1.zfill(max_len)
    bin2 = num2.zfill(max_len)

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


def OctalAdd(num1, num2):
    max_len = max(len(num1), len(num2))
    bin1 = num1.zfill(max_len)  # Дополняем нулями слева для одинаковой длины
    bin2 = num2.zfill(max_len)

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
def OctalSub(num1, num2):
    is_negative = ""
    if int(num1) < int(num2):
        num3 = num1
        num1 = num2
        num2 = num3
        is_negative = "-"

    max_len = max(len(num1), len(num2))
    bin1 = num1.zfill(max_len)
    bin2 = num2.zfill(max_len)

    result = ""
    borrow = 0

    # Проходим по разрядам справа налево
    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin1[i]) + borrow
        bit2 = int(bin2[i])

        if bit1 < bit2:
            # Заимствуем единицу из старшего разряда
            borrow = -1
            bit1 += 8
        else:
            borrow = 0

        result = str(bit1 - bit2) + result



    # Удаляем ведущие нули
    return is_negative + result.lstrip("0") or "0"


def HexAdd(num1, num2):
    hex_characters = "0123456789ABCDEF"
    max_len = max(len(num1), len(num2))
    bin1 = num1.zfill(max_len)  # Дополняем нулями слева для одинаковой длины
    bin2 = num2.zfill(max_len)

    carry = 0
    result = ""

    # Идем от младших разрядов к старшим
    for i in range(max_len - 1, -1, -1):
        bit1 = hex_characters.index(str(bin1[i]))
        bit2 = hex_characters.index(str(bin2[i]))
        sum_bits = bit1 + bit2 + carry
        carry = 0
        if sum_bits > 15:
            sum_bits = sum_bits - 16
            carry = 1
        result = str(hex_characters[sum_bits]) + result  # Остаток от деления на 2

    if carry:
        result = "1" + result

    return result

def HexSub(num1, num2):
    hex_characters = "0123456789ABCDEF"
    # Дополняем нулями для одинаковой длины
    max_len = max(len(num1), len(num2))
    bin1 = num1.zfill(max_len)
    bin2 = num2.zfill(max_len)

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

    if borrow == -1:
        result = "F" + result

    # Удаляем ведущие нули
    return result.lstrip("0") or "0"


if __name__ == "__main__":
	main()