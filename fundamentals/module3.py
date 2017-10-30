# This program takes string input and then prints out a mixed order version of the string
userInput = input('enter a sentence: ')
words = userInput.split()


def wordMixer(words):
    words.sort()
    newWords = []
    while len(words) > 5:
        newWords.append(words.pop(len(words) - 6))
        newWords.append(words.pop(0))
        newWords.append(words.pop(len(words) - 1))

    return newWords


# note im forced to not use 'word in words'
for i in range(len(words)):
    if len(words[i]) <= 3:
        words[i] = words[i].lower()
    elif len(words[i]) >= 7:
        words[i] = words[i].upper()

print(wordMixer(words))
