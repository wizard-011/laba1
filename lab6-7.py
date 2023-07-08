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


#3-esep
sales_data = [
    ("Ivanov", "paper", 10),
    ("Petrov", "pens", 5),
    ("Ivanov", "marker", 3),
    ("Ivanov", "paper", 7),
    ("Petrov", "envelope", 20),
    ("Ivanov", "envelope", 5),
]

# Создание словаря для хранения данных о покупателях и их покупках
customer_data = {}

# Обработка данных о продажах
for sale in sales_data:
    customer = sale[0]
    item = sale[1]
    quantity = sale[2]
    
    # Если покупатель уже существует в словаре, обновляем информацию о его покупке
    if customer in customer_data:
        if item in customer_data[customer]:
            customer_data[customer][item] += quantity
        else:
            customer_data[customer][item] = quantity
    # Если покупатель новый, добавляем его в словарь и записываем информацию о его покупке
    else:
        customer_data[customer] = {item: quantity}

# Сортировка списка покупателей в лексикографическом порядке
sorted_customers = sorted(customer_data.keys())

# Вывод списка покупателей и информации о их покупках
for customer in sorted_customers:
    print(f"{customer}:")
    sorted_items = sorted(customer_data[customer].keys())
    for item in sorted_items:
        quantity = customer_data[customer][item]
        print(f"{item} {quantity}")


#4-esep
def check_access(file_permissions, operation, file_name):
    # Проверка доступа для заданного файла и операции
    if file_name in file_permissions:
        if operation in file_permissions[file_name]:
            return "OK"
    return "Access denied"


# Чтение количества файлов
n = int(input())

# Создание словаря для хранения прав доступа к файлам
file_permissions = {}

# Чтение прав доступа для каждого файла
for _ in range(n):
    file, permissions = input().split()
    file_permissions[file] = set(permissions)

# Чтение количества запросов
m = int(input())

# Обработка запросов
for _ in range(m):
    operation, file = input().split()
    result = check_access(file_permissions, operation, file)
    print(result)


#5-esep
n = int(input())

# Создание словаря для хранения пар синонимов
synonyms = {}

# Чтение пар синонимов и сохранение их в словарь
for _ in range(n):
    word1, word2 = input().split()
    synonyms[word1] = word2
    synonyms[word2] = word1

# Чтение слова, для которого нужно найти синоним
word = input()

# Вывод синонима для данного слова
synonym = synonyms[word]
print(synonym)

#6-esep
# Создание словаря для хранения голосов за кандидатов
votes = {}

# Чтение данных о голосах за кандидатов
while True:
    try:
        candidate, num_votes = input().split()
        num_votes = int(num_votes)
        if candidate in votes:
            votes[candidate] += num_votes
        else:
            votes[candidate] = num_votes
    except EOFError:
        break

# Вывод результатов голосования
for candidate in sorted(votes.keys()):
    print(candidate, votes[candidate])


#7-esep
# Создание словарей для хранения результатов голосования в каждом штате и общих результатов
state_votes = {}
total_votes = {}

# Чтение количества штатов
n = int(input())

# Чтение информации о каждом штате
for _ in range(n):
    state, num_electors = input().split()
    num_electors = int(num_electors)
    state_votes[state] = {"candidates": {}, "electors": num_electors}

# Чтение результатов голосования каждого избирателя
while True:
    try:
        state, candidate = input().split()
        state_votes[state]["candidates"][candidate] = state_votes[state]["candidates"].get(candidate, 0) + 1
        total_votes[candidate] = total_votes.get(candidate, 0) + state_votes[state]["electors"]
    except EOFError:
        break

# Сортировка кандидатов по убыванию числа голосов выборщиков
sorted_candidates = sorted(total_votes.keys(), key=lambda x: (-total_votes[x], x))

# Вывод результатов голосования
for candidate in sorted_candidates:
    print(candidate, total_votes[candidate])
