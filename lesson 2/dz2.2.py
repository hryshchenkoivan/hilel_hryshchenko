chislo = int(input("Введіть 5-значне число: "))

a1 = chislo // 10000
a2 = (chislo % 10000) // 1000
a3 = (chislo % 1000) // 100
a4 = (chislo % 100) // 10
a5 = chislo % 10

reversed_number = a5 * 10000 + a4 * 1000 + a3 * 100 + a2 * 10 + a1

print(reversed_number)