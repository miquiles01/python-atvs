def mensagem1():
    print("Hello word")

def mensagem2():
    return 'Hello word'

mensagem1()

texto = mensagem2()
print(texto)


def lerNotas():
    n = float(input("Digite a primeira nota do aluno: "))
    return n

def resultado1(n1, n2):
    media = (n1+n2) / 2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Média: ", media, "Resultado: ", end="")
    if media >= 7:
        print("Aprovado! Sua média é: ", media)
    else:
        print("Reprovado. Sua média é: ", media)

a = lerNotas()
b = lerNotas()
resultado1(a, b)


