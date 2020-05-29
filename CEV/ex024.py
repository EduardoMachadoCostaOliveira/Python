#Crie um programa que leia o nome de cidade e diga se
#ela começa ou não com o nome "SANTO"
cidade = str(input('Sua cidade: ')).strip()
#Minha Solução
cidade2 = cidade.upper().split()
print('SANTO' in cidade2[0])
#Solução Guanabara
print(cidade[:5].upper() == 'SANTO')
#Soluções Comentários
print('3', 'SANTO' == cidade2[0])
print('4', 'SANTO' in cidade2)
print('Santo' in cidade.title())
print('santo' in cidade.lower().split()[0])
print(cidade.capitalize()[:5] == 'Santo')