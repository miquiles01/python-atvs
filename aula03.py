# if e else
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")


A = input("Informe um valor para a variável A: ")
B = input("Informe um valor para a variável B: ")

if (A<B):
    aux=A;
    A=B;
    B=aux;
print("O valor da variável A agora é: ", A);
print("o valor da variável B agora é: ", B);


nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))

mediaFinal = (nota1 + nota2 + nota3 + nota4) / 4

# verificação
if mediaFinal >= 7.0:
    print("Aluno aprovado!! A sua média é: ", mediaFinal)
else:
    print("Aluno reprovado!! A sua média é: ", mediaFinal)

# elif (qndo tem mais de uma condição)

verificarIdade = int(print("Digite a idade do membro: "))

if verificarIdade > 18:
    print("Classe dos jovens")
elif verificarIdade > 16:
    print("Classe dos Adolescentes")
else:
    print("Outra classe")
