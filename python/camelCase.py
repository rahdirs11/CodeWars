def camel_case(string: str) -> str:
    string = string.strip()
    if len(string) == 0:    return ""
    camelString = str()
    for word in string.split():
        camelString += word.capitalize()
    return camelString

# print(camel_case(input()))
