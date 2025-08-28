maior_media = 0
menor_media = 10
aprovados = 0
reprovados = 0

for i in range(1, 10):
    print(f"\nAluno {i}:")
    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    n3 = float(input("Digite a nota 3: "))
    
    media = (n1 + n2 + n3) / 3
    print(f"Média do aluno {i}: {media:.2f}")
    
    if media > maior_media:
        maior_media = media
    if media < menor_media:
        menor_media = media
    if media >= 6:
        aprovados += 1
    else:
        reprovados += 1

print(f"Maior média: {maior_media:.2f}")
print(f"Menor média: {menor_media:.2f}")
print(f"Alunos aprovados: {aprovados}")
print(f"Alunos reprovados: {reprovados}")