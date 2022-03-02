class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def product(self):
        return self.x * self.y

    def my_sum(self):
        return self.x + self.y

# მომხმარებელს რომ მოუნდეს საპირისპიროდ გამოაკლოს რიცხვები
    def difference(self, key=-1):
        if key != -1:
            return self.y - self.x
        else:
            return self.x-self.y

# მომხმარებელს რომ მოუნდეს საპირისპიროდ გაყოს რიცხვები
    def divide(self, key=-1):
        if key != -1:
            return self.y // self.x
        else:
            return self.x // self.y


task = Calculator(int(input("შემოიტანეთ პირველი რიცხვი: ")), int(input("შემოიტანეთ მეორე რიცხვი: ")))
print(task.my_sum())
print(task.difference())
print(task.product())
print(task.divide())
