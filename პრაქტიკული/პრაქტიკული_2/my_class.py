class Dog:
    def __init__(self, name: str, age: int, color: str):
        self.name = name
        self.age = age
        self.color = color

    def get_values(self):
        return [self.name, self.age, self.color]