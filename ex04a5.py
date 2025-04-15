tentativas= 0
pin= 1234
senha =  int(input("digite sua senha: "))
if senha == pin:
    print("senha bem sucedida")
while senha != pin:
    tentativas+=1
    senha = int(input("digite sua senha: "))

    if tentativas ==2:
        if senha == pin:
            print("senha bem sucedida")
        else:
            print("senha bloqueada")

        break


