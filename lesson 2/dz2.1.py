x= int(input("Введіть число: "))

a1 = x // 1000
a2 = (x % 1000) // 100
a3 = (x % 100) // 10
a4 = x % 10

print(a1)
print(a2)
print(a3)
print(a4)