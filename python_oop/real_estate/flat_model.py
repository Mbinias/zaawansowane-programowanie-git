from real_estate.property_model import Property


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return f"Flat(Address: {self.address}, Floor: {self.floor}, Area: {self.area} sqm, Rooms: {self.rooms}, Price: {self.price} PLN)"
