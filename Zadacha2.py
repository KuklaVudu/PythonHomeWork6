# 2. Фрукты
# Пользователь вводит число K - количество фруктов.
# Затем он вводит K фруктов в формате: название фрукта и его количество.
# Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение.

K = int(input("Количество фруктов: "))
Fruit = {}
for i in range(K):
    name = input("Название фрукта - ")
    age = int(input("Количество - "))
    Fruit[name] = age
print(Fruit)