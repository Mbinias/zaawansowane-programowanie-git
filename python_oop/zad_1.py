"""Stworzyć klasę Student, która posiada 2 parametry (name i marks) oraz jedną metodę is_passed,
która zwraca wartość logiczną, pozytywną gdy średnia ocen jest > 50 w przeciwnym przypadku negatywną.
Następnie należy stworzyć 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda zwracała
true , a dla drugiego false."""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50


student1 = Student("Jan Kowalski", [60, 70, 80])
student2 = Student("Anna Nowak", [40, 30, 20])

print(f"{student1.name} passed: {student1.is_passed()}")
print(f"{student2.name} passed: {student2.is_passed()}")
