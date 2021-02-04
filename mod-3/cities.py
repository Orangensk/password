cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

city = input('Введите город: ')

if city.lower() == tourists[0]['city'].lower():
    print('Турист ' + str(tourists[0]['user']['name']) + ' возраст ' + str(tourists[0]['user']['age']) + '. Посетил город ' + str(tourists[0]['city']) + '.')
elif city.lower() == tourists[1]['city'].lower():
    print('Турист ' + str(tourists[1]['user']['name']) + ' возраст ' + str(tourists[1]['user']['age']) + '. Посетил город ' + str(tourists[1]['city']) + '.')
elif city.lower() == tourists[2]['city'].lower():
    print('Турист ' + str(tourists[2]['user']['name']) + ' возраст ' + str(tourists[2]['user']['age']) + '. Посетил город ' + str(tourists[2]['city']) + '.')
else:
    print('Такого города нет в нашем списке!')
