class MyList:
    def __init__(self, data: list): self.data = data

    def __mul__(self, other):
        return self.data * other

    def __add__(self, other):
        return self.data + other.data

    def __str__(self):
        return f"{self.data}"


test_list1 = MyList([1, 2, 3])
test_list2 = MyList([5, 6, 7])

print(test_list1 * 2)
print(test_list1 + test_list2)
print(str(test_list1))
