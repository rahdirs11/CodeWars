def pig_it(text: str) -> str:
    output, word = str(), str()
    for c in text:
        if c.isalpha():
            word += c
        elif c == ' ':
            output += word[1: ] + word[0] + 'ay '
            word = str()
        else:   output += c

    return output if len(word) == 0 else output + word[1: ] + word[0] + 'ay'

print(pig_it(input()))
