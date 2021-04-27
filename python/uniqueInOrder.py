from itertools import groupby

def unique_in_order(iterable):
    output = list()
    for key, group in groupby(iterable):
        output.append(key)
    return output
