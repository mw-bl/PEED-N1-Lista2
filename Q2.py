nomes = ()

for i in range(3):
    nome = (input("Digite um nome: "))
    nomes += (nome,)

print("Nomes inseridos: ", nomes)

indice = int(input("Escolha o indice (1, 2 ou 3) do nome que deseja substituir: ")) - 1

novoNome = input("Digite o novo nome: ")

nomes = nomes[:indice] + (novoNome,) + nomes[indice+1:]

print("Nova tupla de nomes:", nomes)
