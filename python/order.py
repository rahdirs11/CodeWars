def order(sentence):
    words = sentence.split()
    if len(words) == 0:
        return ''
    numWord = []
    for word in words:
        x = sorted(word)
        numWord.append([int(x[0]), word])
    return ' '.join(map(lambda x: x[1], sorted(numWord, key = lambda x: x[0])))
