qntd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qntd = qntd + 1
    # Entrada
    valor = float(input("Digite um valor: "))

media = qntd / soma
print("\n total da soma: ", soma)
print("\n quantidade de valores digitados: ", qntd)
print("\n media de valores: ", media)