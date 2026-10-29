"""2. Utwórz funkcję, która **otrzyma w parametrze** listę zawierającą 5 dowolnych liczb,
każdy jej element pomnoży przez 2, a na końcu ją **zwróci.** Zadanie należy wykonać w 2 wersjach:
1. Wykorzystując pętle `for`.
2. Wykorzystując listę składaną.
"""


def multiply_numbers_for_loop(numbers: list[int]) -> list[int]:
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


def multiply_numbers2(numbers: list[int]) -> list[int]:
    return [number * 2 for number in numbers]


if __name__ == "__main__":
    numbers_list = [1, 2, 3, 4, 5]
    multiplied_for_loop = multiply_numbers_for_loop(numbers_list)
    multiplied_comprehension = multiply_numbers2(numbers_list)

    print("Wynik z pętli for:", multiplied_for_loop)
    print("Wynik z listy składanej:", multiplied_comprehension)
