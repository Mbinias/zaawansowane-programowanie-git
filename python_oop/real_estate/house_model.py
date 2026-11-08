from real_estate.property_model import Property


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return f"House(Address: {self.address}, Area: {self.area} sqm, Rooms: {self.rooms}, Plot: {self.plot} sqm, Price: {self.price} PLN)"
