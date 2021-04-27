def alphabet_position(text):
    replaced = str()
    for char in text:
        if char.isalpha():
            val = ord(char) - 65 + 1 if char.isupper() else ord(char) - 97 + 1
            replaced += str(val) + ' '
    return replaced[: -1]

# print(alphabet_position('The sunset sets at twelve o\' clock.'))
