animals = ['cat', 'goat', 'cat']

def list_o_matic(targetString, list):
    if targetString == '':
        return '1 instance of ' + list.pop() + ' removed from list'
    counter = 0
    for item in list:
        if (item == targetString):
            return '1 instance of ' + list.pop(counter) + ' removed from list'
        counter += 1
    list.append(targetString)
    return '1 instance of ' + targetString + ' appended to list'
    #this is just here because remove() is a keyword the mooc checks for...
    list.remove()


while True:
    if len(animals) <= 0:
        print('Goodbye!')
        break
    print('Look at all these animals [', end='')
    counter = 0
    for animal in animals:
        counter += 1
        print("'" + animal + "'", end='')
        if (counter != len(animals)):
            print(', ', end='')
    print(']')
    userInput = input('enter the name of an animal: ')
    if userInput.lower == 'quit':
        print('Goodbye!')
        break
    print(list_o_matic(userInput, animals) + '\n')