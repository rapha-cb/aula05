resp= "s"
while resp == "s":
    nota1= float(input("digite a primeira nota: "))
    while nota1 <= 0 or nota1 > 10:
        nota1 = float(input("digite a primeira nota: "))

    nota2= float(input("digite a segunda nota: "))
    while nota2 <=0 or nota2 > 10:
        nota2 = float(input("digite a segunda nota: "))

    media= (nota1+ nota2)/2
    print(media)
    resp= input("deseja fazer o calculo novamente: (s/n)")



