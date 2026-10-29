# Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie wyświetli każde z nich.


def print_names(names: list[str]) -> None:
    for name in names:
        print(name)


if __name__ == "__main__":
    names_list = ["Mariusz", "Tomasz", "Krzysztof", "Michał", "Piotr"]
    print_names(names_list)
