def to_camel_case(text):
    #your code here
    if len(text) == 0:    return ''
    words = list()
    if '-' in text and '_' in text:
        words = text.split('-')
        for w in words:
            if '_' in w:
                words += w.split('_')
                break
    elif '-' in text:
        words = text.split('-')
    else:   words = text.split('_')
    print(words)
    return words[0] + ''.join(map(lambda x: x.capitalize, words[1: ]))

print(to_camel_case(input()))
