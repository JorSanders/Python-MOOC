def get_names():
    elements = []
    while len(elements) < 5:
        userInput = input('Enter the name of an element: ').strip().lower()
        if not userInput in elements and not userInput == '':
            elements.append(userInput)
    return elements


import urllib.request

# Download the file from `url` and save it locally under `file_name`:
url = 'https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt'
file_name = 'elements1_20.txt'
urllib.request.urlretrieve(url, file_name)
userElements = []
correct = []
incorrect = []

elements_file = open(file_name, 'r')
elements = elements_file.readlines()

for i, element in enumerate(elements):
    elements[i] = element.strip().lower()

userElements = get_names()

for element in userElements:
    if element in elements:
        correct.append(element)
    else:
        incorrect.append(element)

percentage = len(correct) / len(userElements) * 100

print('')

print(str(percentage) + '% correct\n')
print('found: ')
for element in correct:
    print(element, ' ')

print('')

print('not found: ')
for element in incorrect:
    print(element, ' ')

print('')

elements_file.close()
