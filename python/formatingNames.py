def namelist(names):
    nameList = [d['name'] for d in names]
    return '' if len(nameList) == 0 else (nameList[-1] if len(nameList) == 1 else ', '.join(nameList[: -1]) + ' & ' + nameList[-1])
#     if len(names) == 0:
#         return ''
#     elif len(names) == 1:
#         return names[0]['name']
#     nameList = [d['name'] for d in names]
#     return ', '.join(nameList[: -1]) + ' & ' + nameList[-1]
