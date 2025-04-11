'''from abc import ABC, abstractmethod

# Определение абстрактного класса Vehicle
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        """Запуск двигателя"""
        pass

    @abstractmethod
    def stop_engine(self):
        """Останавка двигателя"""
        pass

# Подкласс Car, наследуемый от Vehicle
class Car(Vehicle):

    def start_engine(self):
        print("Двигатель автомобиля запущен")

    def stop_engine(self):
        print("Двигатель автомобиля остановлен")

# Подкласс Bike, наследуемый от Vehicle
class Bike(Vehicle):

    def start_engine(self):
        print("Двигатель мотоцикла запущен")

    def stop_engine(self):
        print("Двигатель мотоцикла остановлен")

# Создаем экземпляры классов
my_car = Car()
my_bike = Bike()

# Вызываем методы для автомобиля
my_car.start_engine()  #Двигатель автомобиля запущен
my_car.stop_engine()   #Двигатель автомобиля остановлен

# Вызываем методы для мотоцикла
my_bike.start_engine()  #Двигатель мотоцикла запущен
my_bike.stop_engine()   #Двигатель мотоцикла остановлен'''

'''# Список словарей
people = [
    {'name': 'Вова', 'age': 19},
    {'name': 'Настя', 'age': 20},
    {'name': 'Марк', 'age': 199},
    {'name': 'Николай', 'age': 18}
]

# Сортировка списка словарей по ключу age
sorted_people = sorted(people, key=lambda x: x['age'])

print("Сортированный список по возрасту: ")
for person in sorted_people:
    print(person)

# Функция для проверки, является ли число простым
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Список чисел
numbers = [11, 15, 23, 44, 7, 10, 19, 2, 1, 199]

# Фильтрация списка чисел, оставляя только простые числа
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("\nСписок простых чисел:")
print(prime_numbers)'''


'''class BankAccount:
    def __init__(self, nach_balance=0):
        self.__balance = nach_balance  # Приватное поле для хранения баланса

    def deposit(self, amount):
        """Метод для пополнения счета."""
        if amount > 0:
            self.__balance += amount
            print(f"Пополнение на {amount}. Текущий баланс: {self.__balance}")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        """Метод для снятия средств"""
        if amount > self.__balance:
            print("Ошибка: недостаточно средств на счете")
        elif amount <= 0:
            print("Сумма снятия должна быть положительной")
        else:
            self.__balance -= amount
            print(f"Снятие {amount}. Текущий баланс: {self.__balance}")

    def get_balance(self):
        """Метод для получения текущего баланса."""
        return self.__balance

# Создаем экземпляр класса
account = BankAccount(100)  # Создаем счет с начальным балансом 100

# Выполняем операции пополнения/снятия с банковским счетом
account.deposit(150)   # Пополняем счет на 150
account.withdraw(50)   # Снимаем 50
account.withdraw(201)  # Пытаемся снять 201 (должна быть ошибка, т.к не достаточно на балансе)
print(f"Текущий баланс: {account.get_balance()}")  # Выводим текущий баланс'''

