print("    MENU     ")
print("escolha uma opção.Para encerrar digite sair")
print("1.soma")
print("2.subtração")
print("3.multiplicação")
print("4.divisão")
print("5.par ou ímpar")
print("6.fatorial")
print("7.primo")
opcao=input("Digite a opção desejada ou sair para encerrar: ")
while opcao!="SAIR" or "Sair" or "sair":
    if opcao=="1":
        numero1=int(input("Digite o primeiro valor: "))
        numero2=int(input("Digite o segundo valor: "))
        print("O resultado da soma é",numero1+numero2)
    if opcao=="2":
        numero1=int(input("Digite o primeiro valor: "))
        numero2=int(input("Digite o segundo valor: "))
        print("O resultado da Subtração é",numero1-numero2)
    if opcao=="3":
        numero1=int(input("Digite o primeiro valor: "))
        numero2=int(input("Digite o segundo valor: "))
        print("O resultado da multiplicação é",numero1*numero2)
    if opcao=="4":
        numero1=int(input("Digite o primeiro valor: "))
        numero2=int(input("Digite o segundo valor: "))
        print("O resultado da divisão é",numero1/numero2)
    if opcao=="5":
        numero=int(input("Digite um valor para saber se ele é ímpar ou par: "))
        if numero%2==0:
            print("O número",numero,"é par")
        else:
            print("O número",numero,"é ímpar")
    print("escolha uma opção.Para encerrar digite sair")
    print("1.soma")
    print("2.subtração")
    print("3.multiplicação")
    print("4.divisão")
    print("5.par ou ímpar")
    print("6.fatorial")
    print("7.primo")
    input("Pressione ENTER para voltar ao MENU")
    opcao=input("Digite a opção desejada ou sair para encerrar: ")
