def abbreviate(words):
    words = words.replace('-', ' ')
    line = words.split()
    letters = [word[0] for word in line]
    return "".join(letters).upper()
