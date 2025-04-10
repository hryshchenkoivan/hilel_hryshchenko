x= int(input("Введіть число: "))

b1 = x // 1000
b2 = (x % 1000) // 100
b3 = (x % 100) // 10
b4 = x % 10

print("Ваше число: ")
print(b1)
print(b2)
print(b3)
print(b4)