"""1. Stworzyć następujące klasy:
- Property (klasa opisująca posiadłość/nieruchomość), posiadająca pola:
    - area
    - rooms (int)
    - price
    - address
- House (klasa dziedzicząca klasę `Property`, która opisuje dom), posiadająca pola:
    - plot (rozmiar działki, int)
- Flat (klasa dziedzicząca klasę `Property`, która opisuje mieszkanie), posiadająca pola:
    - floor

Dodatkowo:

- Każda z klas dziedziczących ma mieć zaimplementowaną metodę `__str__` , która będzie opisywała
obiekt.
- Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy
za pośrednictwem konstruktora.
- Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je wyświetlić."""


class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property at {self.address}: {self.area} m2, {self.rooms} rooms, ${self.price}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House at {self.address}: {self.area} m2, {self.rooms} rooms, ${self.price}, Plot: {self.plot} m2"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat at {self.address}: {self.area} m2, {self.rooms} rooms, ${self.price}, Floor: {self.floor}"


house = House(200, 5, 300000, "123 Main St", 500)
flat = Flat(80, 3, 150000, "456 Elm St", 2)

print(house)
print(flat)
