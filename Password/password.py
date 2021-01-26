a = input('Введите пароль: ')
b = 2

try:
    c = len(a)
    result = b/c
    d = int(a)
    result = d/b
    print('Ваш пароль состоит только из цифр')
except ZeroDivisionError:
    print('Вы ввели пустой пароль')
except ValueError:
    print('Требования к паролю соблюдены')
