def increment_string(strng):
    number, i = list(), len(strng) - 1
    while strng[i].isdigit():
        number.append(strng[i])
        i -= 1
    length = len(number)
    if length == 0:
        return strng + '1'
    else:
        number.reverse()
        number = ''.join(number)
        # print(len(number), end=' ')
        intNumber = int(number) + 1
        # print(len(str(intNumber)))
        if len(str(intNumber)) != len(number):
            i += abs(len(number) - len(str(intNumber)))
        return f'{strng[: i + 1]}{intNumber}'
