nums = input("Digite 10 números separando-os por espaçoa: ")

lnums = [int(n) for n in nums.split()]

cjNums = set(lnums)
spar = set()
for num in cjNums:
    if num % 2 != 0:
        spar.add(num)

print("Conjunto sem os números pares:", spar)