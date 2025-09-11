soma = 0
contador = 1
N = int(input("Digite um número: "))
while contador <= N:
	soma += contador
	contador += 1
print("A soma dos números de 1 até", N, "é:", soma)