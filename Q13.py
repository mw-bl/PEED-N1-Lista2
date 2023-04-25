dic = {}

while True:
    chave = input("Digite a chave do dicionário (ou 'sair' para encerrar): ")
    if chave == 'sair':
        break
    valor = input("Digite o valor correspondente: ")
    dic[chave] = valor

if 'profissão' in dic:
    print("A chave 'profissão' está presente no dicionário")
else:
    print("A chave 'profissão' não está presente no dicionário")