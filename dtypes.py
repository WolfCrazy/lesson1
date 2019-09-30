a = 5
b = 2
print('a=', a)
print('b=', b)
print('a + b = ' + str(a+b))
print('a - b = ' + str(a-b))
print('a * b = ' + str(a*b))
print('a ^ b = ' + str(a**b))
print('a / b = ' + str(a/b))
print('a // b = ' + str(a//b))
print('a > b = ' + str(a > b))
print('a < b = ' + str(a < b))

a = 'Привет'
b = 'мир'
c = 33
print(a + ' ' + b + '!')
print('{} {}!'.format(a, b))
print('{} {}!{}'.format(a, b, c))
n = 'Миша'
print('Привет, {name}'.format(name=n))
print(f'Привет, {n}!')
print(len(f'{a} {b}!'))
print('привет'.upper())
print('пРиВет'.lower())
print('привет мир'.capitalize())
print('        привет           '.strip())
print('        привет           '.rstrip())
print('прив3т т3б3'.replace('3', 'е'))
print('Привет.Мир.Миша'.split('.'))
print(None)
print(a is None)
print(b is not None)
print(type(a))
print(type(None))
name = input('Введите число: ')
print(name, type(name))
name = int(name)
print(name, type(name))


