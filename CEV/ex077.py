palavras = ('Curso', 'Video', 'Internet', 'Gratis', 'Futuro', 'Eeeeduardooooooo')
for p in palavras:
    print(f'\nNa palavra {p.upper():_^12} temos as vogais:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
