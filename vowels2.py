"vowels = {'a','e','i','o','u'}"
vowels = set('aeiou')
word = input('provide a word to search for vowels: ')
found =vowels.intersection(set(word))
for vowel in found:
    print(vowel)
