def str_analysis(str1):
    # only alpha
    if (str1.isalpha()):
        return ' all alphabetic'
        # numeric
    elif (str1.isnumeric()):
        tmp = int(str1)
        if (tmp > 99):
            return str1 + ' big number'
        else:
            return str1 + ' small number'
    else:
        return ' multiple character types'


while True:
    userInput = input('enter word or integer: ')
    if (userInput == ''):
        continue

    print(str_analysis(userInput))
    break;
