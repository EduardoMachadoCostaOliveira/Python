#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros
n1 = float(input("Uma distância em metros: "))
print(f'A medidade de {n1}m, corresponde a ')
#Mostrar tambem quantidade de Kilometros, hectometros, decametros, decimetros,
km = n1 / 1000
print(f'{km}km -        Kilometros')
hm = n1 / 100
print(f'{hm}hm -        Hectometros')
dam = n1 / 10
print(f'{dam}dam -      Decametros')
dm = n1 * 10
print(f'{dm:.0f}dm -        Decimetros')
cm = n1 * 100
print(f'{cm:.0f}cm -        Centimetros')
mm: float = n1 * 1000
print(f'{mm:.0f}mm -        Milimetros')