"""Rozszerzyć skrypt z punktu 7 o przyjmowanie parametru city , który może być przekazywany w wierszu
poleceń podczas wykonywania (np. python main.py --city=Berlin ). Należy wykorzystać moduł argparse do
wczytywania przekazywanych parametrów, a w razie przekazania wartości ograniczyć pobierane browary do
miasta, które zostało wskazane."""

import requests
import argparse


class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, street: str, city: str, state: str, postal_code: str, country: str, longitude: str, latitude: str, phone: str, website_url: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url

    def __str__(self) -> str:
        return f"Brewery ID: {self.id}, Name: {self.name}, Type: {self.brewery_type}, Address: {self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}, Phone: {self.phone}, Website: {self.website_url}"


def fetch_breweries(city: str = None) -> list:
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": 20}
    if city:
        params["by_city"] = city

    response = requests.get(url, params=params)
    data = response.json()
    breweries_list = []

    for item in data:
        brewery = Brewery(
            id=item.get("id"),
            name=item.get("name"),
            brewery_type=item.get("brewery_type"),
            street=item.get("street"),
            city=item.get("city"),
            state=item.get("state"),
            postal_code=item.get("postal_code"),
            country=item.get("country"),
            longitude=item.get("longitude"),
            latitude=item.get("latitude"),
            phone=item.get("phone"),
            website_url=item.get("website_url"),
        )
        breweries_list.append(brewery)

    for b in breweries_list:
        print(b)
    return breweries_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch breweries from Open Brewery DB")
    parser.add_argument("--city", type=str, help="Filter breweries by city")
    args = parser.parse_args()

    fetch_breweries(city=args.city)
