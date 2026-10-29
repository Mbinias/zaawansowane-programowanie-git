"""Stworzyć skrypt pythonowy, który połączy się z API, które zawiera informacje o browarach
(dokumentacja https://www.openbrewerydb.org/documentation).
Należy w pythonie zrobić klasę Brewery, która będzie zawierała takie atrybuty jakich dostarcza API
wraz z odpowiednim typowaniem. W klasie należy zaimplementować magiczną metodę __str__ która będzie
opisywała dane przechowywane w obiekcie. Skrypt ma się połączyć do API i pobrać 20 pierwszych obiektów,
a następnie utworzyć listę 20 instancji klasy Brewery, którą przeiteruje i wyświetli każdy obiekt
z osobna."""

import requests


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
        return (
            f"Brewery ID: {self.id}, Name: {self.name}, Type: {self.brewery_type}, "
            f"Address: {self.street}, {self.city}, {self.state}, {self.postal_code}, "
            f"{self.country}, Phone: {self.phone}, Website: {self.website_url}"
        )


def fetch_breweries() -> list:
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": 20}
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


if __name__ == "__main__":
    fetch_breweries()
