orderWeight = float(input('Enter cheese order weight (numeric value): '));
max = 100;
min = 5;
price = 34.5
if (orderWeight > max):
    print(str(orderWeight) + ' is more than currently available in stock');
elif (orderWeight < min):
    print(str(orderWeight) + ' below minimum order amount');
else:
    print(str(orderWeight) + ' costs €' + str(orderWeight * price));
