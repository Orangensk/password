new_list = [1, 2, 3]

if type(new_list) == int or type(new_list) == float:
    print('Это число')
elif type(new_list) == tuple:
    print('Это кортеж')
elif type(new_list) == dict:
    print('Это словарь')
elif type(new_list) == list:
    print('Это список')
elif type(new_list) == str:
    print('Это строка')
else:
    print('такой тип я не знаю')
