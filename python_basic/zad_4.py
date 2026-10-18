'''Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane wykorzystanie funkcji range), a następnie wyświetli co drugi element.'''

def print_every_second_number(numbers: list[int]) -> None:
    for i in range(1, len(numbers), 2):
        print(numbers[i])

if __name__ == "__main__":
    numbers_list = list(range(1, 11))
    print_every_second_number(numbers_list)