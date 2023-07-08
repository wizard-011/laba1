#1-esep
'''# Список
students_list = ["John", "Mary", "Alex"]

# Кортеж
students_tuple = ("Peter", "Emily", "Tom")

# Множество
students_set = {"Kate", "Michael", "Sophie"}

# Словарь
students_dict = {
    "ID1": "David",
    "ID2": "Emma",
    "ID3": "Oliver"
}

# Вывод списка
print("Список студентов:")
for student in students_list:
    print(student)

# Вывод кортежа
print("\nКортеж студентов:")
for student in students_tuple:
    print(student)

# Вывод множества
print("\nМножество студентов:")
for student in students_set:
    print(student)

# Вывод словаря
print("\nСловарь студентов:")
for student_id, student_name in students_dict.items():
    print(f"ID: {student_id}, Имя: {student_name}")'''

#2-esep
# Список
my_list = [1, 2, 3, 4, 5]

# Кортеж
my_tuple = (6, 7, 8, 9, 10)

# Множество
my_set = {11, 12, 13, 14, 15}

# Словарь
my_dict = {"a": 16, "b": 17, "c": 18, "d": 19, "e": 20}

# Общие методы для всех типов данных
print("Общие методы:")
print("Длина:", len(my_list))
print("Максимум:", max(my_tuple))
print("Минимум:", min(my_set))
print("Сумма:", sum(my_dict.values()))
print("Наличие элемента в словаре:", "a" in my_dict)

# Методы, специфичные для типа данных
print("\nМетоды, специфичные для типа данных:")
print("Список:")
print("Индекс элемента 2:", my_list.index(2))
print("Количество элементов 3:", my_list.count(3))

print("\nКортеж:")
print("Индекс элемента 9:", my_tuple.index(9))
print("Количество элементов 10:", my_tuple.count(10))

print("\nМножество:")
my_set.add(16)
print("Множество после добавления элемента 16:", my_set)

print("\nСловарь:")
my_dict.pop("b")
print("Словарь после удаления ключа 'b':", my_dict)
