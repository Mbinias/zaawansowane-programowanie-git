"""Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane wykorzystanie funkcji range),
a następnie wyświetli jedynie parzyste elementy."""


def print_even_numbers(numbers: list[int]) -> None:
    for number in numbers:
        if number % 2 == 0:
            print(number)


if __name__ == "__main__":
    numbers_list = list(range(1, 11))
    print_even_numbers(numbers_list)
