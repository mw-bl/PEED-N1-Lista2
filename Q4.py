nums = set()
for i in range(5):
    num = int(input("Digite um número: "))
    nums.add(num)

print("O conjunto é: ", nums)

numRemove = int(input("Digite um número para remover do conjunto: "))
if numRemove in nums:
    nums.remove(numRemove)
    print("O número", numRemove, "foi removido do conjunto.")
else:
    print("O número", numRemove, "não está presente no conjunto.")

print("O conjunto atualizado é: ", nums)