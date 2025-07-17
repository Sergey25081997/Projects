# Домашнее задание. Цепочкка наследований (5 классов), используя атрибуты и методы, а так же super().
class Animal:
    """Базовый класс животного."""

    def __init__(self, species):
        self.species = species


class Mammal(Animal):
    """Млекопитающее — наследник Animal."""

    def __init__(self, species, has_fur):
        super().__init__(species)
        self.has_fur = has_fur


class Carnivore(Mammal):
    """Хищник — наследник Mammal."""

    def __init__(self, species, has_fur, can_hunt):
        super().__init__(species, has_fur)
        self.can_hunt = can_hunt


class Feline(Carnivore):
    """Кошачьи — наследник Carnivore."""

    def __init__(self, species, has_fur, can_hunt, can_climb):
        super().__init__(species, has_fur, can_hunt)
        self.can_climb = can_climb


class Cat(Feline):
    """Домашняя кошка — наследник Feline."""

    def __init__(self, species, has_fur, can_hunt, can_climb, name):
        super().__init__(species, has_fur, can_hunt, can_climb)
        self.name = name


# Пример использования
if __name__ == "__main__":
    my_cat = Cat("Кошка", True, True, True, "Мурка")
    print(f"Вид: {my_cat.species}")
    print(f"Есть шерсть: {my_cat.has_fur}")
    print(f"Умеет охотиться: {my_cat.can_hunt}")
    print(f"Умеет лазать: {my_cat.can_climb}")
    print(f"Имя: {my_cat.name}")
