class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return f"Property(Address: {self.address}, Area: {self.area} sqm, Rooms: {self.rooms}, Price: {self.price} PLN)"
