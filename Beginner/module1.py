foodEaten = input('What food have you eaten in the last 24 hours?: ');

foodCatagories = ['dairy', 'nuts', 'seafood'];
for foodCatagorie in foodCatagories:
    if (foodCatagorie.lower() in foodEaten.lower()):
        print('is it True that' + foodEaten + ' contains ' + ' contains ' + foodCatagorie);
    if ('dairy'.lower() in foodEaten.lower()):
        print('True');
    else:
        print('false');
    if ('nuts'.lower() in foodEaten.lower()):
        print('True');
    else:
        print('false');
    if ('seafood'.lower() in foodEaten.lower()):
        print('message');
    if ('chocolate'.lower() in foodEaten.lower()):
        print('message');
