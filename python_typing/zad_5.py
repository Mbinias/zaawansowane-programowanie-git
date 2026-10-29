"""Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list, a drugi typu int .
Funkcja ma sprawdzić (zwracając typ logiczny bool), czy lista z parametru pierwszego zawiera
taką wartość jaką przekazano w parametrze drugim."""


def contains_value(lst: list, value: int) -> bool:
    for item in lst:
        if item == value:
            return True
    return False


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    value_to_check = 3
    result = contains_value(my_list, value_to_check)
    print(result)
