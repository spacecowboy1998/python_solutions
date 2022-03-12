class MinMax(list):

    def min(self):
        minimum = 9999
        for element in self:
            if element < minimum:
                minimum = element
        return minimum

    def max(self):
        maximum = -9999
        for element in self:
            if element > maximum:
                maximum = element
        return maximum


numbers_list = MinMax()
for number in input("შემოიტანეთ თქვენი სიის ელემენტები: ").split():
    numbers_list.append(int(number))

print(numbers_list.max())
print(numbers_list.min())
