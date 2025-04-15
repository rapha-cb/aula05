nota1= int(input("digite a primeira nota: "))
while nota1 <= 0 or nota1 > 10:
    nota1 = int(input("digite a primeira nota: "))

nota2= int(input("digite a segunda nota: "))
while nota2 <=0 or nota2 > 10:
    nota2 = int(input("digite a segunda nota: "))

media= (nota1+ nota2)/2
print(media)