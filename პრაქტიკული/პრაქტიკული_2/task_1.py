class Fruit:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight

    def __eq__(self, other):
        return self.name == other.name


fruit1 = Fruit("apple", 21)
fruit2 = Fruit("banana", 55)
fruit3 = Fruit("apple", 18)

print(fruit1 + fruit2)
print(fruit1 == fruit3)
print(fruit1 == fruit2)

