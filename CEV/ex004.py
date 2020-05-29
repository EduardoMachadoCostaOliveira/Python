#ex004
a = input('Digite algo: ')
print(f'O tipo primitivo de {a} é ', type(a))
print(f'{a}, só tem espaços?', a.isspace())
print(f'{a}, é um número? ', a.isnumeric())
print(f'{a}, é alfabético? ', a.isalpha())
print('É alphanumerico?', a.isalnum())
# Maneiras Alternativas
print('{}, está em maiúsculas? {}'.format(a, a.isupper()))
print('{}, está em minúculas?'.format(a), a.islower())
print('Está capitalizada? {}'.format(a.istitle()))




