# aks the user for input prints all words that start with an h

# If you actually ask users for input like this ill stab you
userQuote = input('Enter a 1 sentence quote, non-alpha separate words:')
word = ''
# Note that the last word wont be printed if you dont end the string with non alpha character
for character in userQuote:
    if character.isalpha():
        word += character
    else:
        if len(word) > 0 and word.upper()[0] >= 'H':
            print(word.upper())
            word = ''
