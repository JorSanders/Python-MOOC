def fishstore(fish, price):
    return 'fish type: ' + fish + ' cost: €' + str(price);


fish = input('What fish would you like: ');
price = input('What price would you like: ');
print(fishstore(fish, price));
