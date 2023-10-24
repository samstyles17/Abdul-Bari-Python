def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


n = int(input())
words = input().split()
print(score_words(words))