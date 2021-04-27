def solution(s):
    s = s + '_' if len(s) % 2 != 0 else s
    output = list()
    for i in range(0, len(s), 2):
        output += s[i: i+2]
    return output
