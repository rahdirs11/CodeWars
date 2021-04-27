def generate_hashtag(s: str) -> str:
    if len(s) == 0 or len(s) > 140: return 'False'
    output = '#' + ''.join(map(lambda x: x.capitalize() if len(x) != 0 else '', s.split()))
    return output

print(generate_hashtag(input()))
