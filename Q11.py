nums = []

for i in range(10):
    num = int(input("Digite um número: "))
    nums.append(num)

print("Números pares:")
for i in range(0, len(nums), 2):
    print(nums[i])