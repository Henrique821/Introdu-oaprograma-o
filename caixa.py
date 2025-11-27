total=0
quant=0
mcaro=0
continuar="s"
while continuar=="s":
    preco=float(input("informe o preço do produto: "))
    while preco<0:
        print("preço inválido! informe um preço válido")
        preco=float(input("informe o preço do produto: "))
        total+=preco
        quant+=1
        if preco>mcaro:
            mcaro=preco
    continuar=input("deseja continuar? (s/n) ")
while continuar!="s" and continuar!="n":
   print("opção inválida! informe s para sim ou n para não")
   continuar=input("deseja continuar? (s/n) ")
   if quant>0:
    media=total/quant
    media=0
else:
    media=0
print("resumo das compras")
print("total gasto: R$"(total))
print("quantidade de produtos comprados: "(quant))
print("média de preços dos produtos: R$"(media))
print("preço do produto mais caro: R$"(mcaro))