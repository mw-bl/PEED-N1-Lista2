num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))

nums = {num1, num2, num3, num4, num5}

if 3 in nums:
    print("O número 3 está presente no conjunto")
else:
    print("O número 3 não está presente no conjunto")