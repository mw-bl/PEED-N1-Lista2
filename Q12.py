nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")

nomes = (nome1, nome2, nome3)

if 'Maria' in nomes:
    print("O nome Maria está presente na tupla")
else:
    print("O nome Maria não está presente na tupla")