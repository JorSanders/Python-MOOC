total = 0
items = 'Items'


def adding_report(type='T'):
    global total
    global items
    while True:
        userInput = input('Enter an integer or "Q": ')
        if userInput.isdigit():
            total += int(userInput)
            if (type == 'A'):
                items += '\n' + userInput;
            elif userInput.lower().startswith('q'):
                print('\n')
            if (type == 'A'):
                print(items + '\n')
                print('Total \n' + str(total))
                break;
        else:
            print('Invalid input')

adding_report('A')
adding_report('T')
