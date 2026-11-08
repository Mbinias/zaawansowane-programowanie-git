from real_estate.house_model import House
from real_estate.flat_model import Flat

if __name__ == "__main__":
    my_house = House(area=150.5, rooms=5, price=1200000.0, address="12 Spring St, Warsaw", plot=1000)
    my_flat = Flat(area=65.0, rooms=3, price=800000.0, address="4/12 Autumn St, Krakow", floor=2)

    print("--- Modular Object Import Result ---")
    print(my_house)
    print(my_flat)
