import urllib.request

# Download the file from `url` and save it locally under `file_name`:
url = 'https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv'
file_name = 'world_temp_mean.txt'
urllib.request.urlretrieve(url, file_name)

temperatures_file = open(file_name, 'a+')
temperatures_file.write('Rio de Janeiro,Brazil,30.0,18.0\n')

temperatures_file.seek(0, 0)
headings = temperatures_file.readline().strip()
headings = headings.split(',')

while True:
    city_temp = temperatures_file.readline().strip()
    if city_temp == '':
        break
    city_temp = city_temp.split(',')

    print(headings[2] + ' for ' + city_temp[0] + ' is ' + city_temp[2] + ' Celsius')

temperatures_file.close()