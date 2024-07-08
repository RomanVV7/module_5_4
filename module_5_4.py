#Задача "История строительства" (на основе предыдущей задачи

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors


    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if new_floor < 1 or new_floor > self.numbers_of_floors:
                print('Такого этажа не существует')
                break
            else:
                print(i)

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numbers_of_floors}'

    def __eq__(self, other):
        return self.numbers_of_floors == other.numbers_of_floors

    def __lt__(self, other):
        return self.numbers_of_floors < other.numbers_of_floors

    def __le__(self, other):
        return self.numbers_of_floors <= other.numbers_of_floors

    def __gt__(self, other):
        return self.numbers_of_floors > other.numbers_of_floors

    def __ge__(self, other):
        return self.numbers_of_floors >= other.numbers_of_floors

    def __ne__(self, other):
        return self.numbers_of_floors != other.numbers_of_floors

    def __add__(self, value):
        self.numbers_of_floors = self.numbers_of_floors + value
        return self


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрешки', 20)
print(House.houses_history)

#Удаление объектов
del h2
del h3

print(House.houses_history)
