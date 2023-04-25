dic = {}

for i in range(3):
    chave = input("Digite a chave do dicionário: ")
    valor = input("Digite o valor do dicionário: ")
    dic[chave] = valor

dic['cidade'] = input("Digite a cidade em que você nasceu: ")

print("O dicionário atualizado é:", dic)