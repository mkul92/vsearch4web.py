def search4vowels(phrase: str) -> set:
    "return vowels in a given phrase"
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    "return a set of letters found in given phrase"
    return set(letters).intersection(set(phrase))
