# # Пример функции вычисления факториала числа
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# # Вызов функции и вывод результата
# print(factorial(5))  # Выводит 120
#============================================================
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
    
#     def accelerate(self, speed_increase):
#         self.speed += speed_increase
    
#     def brake(self, speed_decrease):
#         if self.speed >= speed_decrease:
#             self.speed -= speed_decrease
#         else:
#             self.speed = 0
    
#     def get_speed(self):
#         return self.speed

# # Создание объекта класса Car и вызов его методов
# car = Car("Toyota", "Camry", 2021)
# car.accelerate(20)
# print(car.get_speed())  # Выводит 20

# car.brake(10)
# print(car.get_speed())  # Выводит 10

# car.brake(15)
# print(car.get_speed())  # Выводит 0
#======================================================================
# def sirtki(a):
#     b = a
#     def ishki():
#         c = 12
#         print(int (b)+ int (c))

#     # print(c) #это ошибка потому что внешная фукция не имеет доступ к внутр
#     ishki()

# a= 13
# sirtki(a)
