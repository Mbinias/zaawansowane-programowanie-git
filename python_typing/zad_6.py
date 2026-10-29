"""Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list.
Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty, każdy element podnieść
do potęgi 3 stopnia, a następnie zwrócić powstałą listę."""


def process_lists(list1: list, list2: list) -> list:
    combined_list = list1 + list2
    unique_list = list(set(combined_list))
    result_list = [x**3 for x in unique_list]
    return result_list


if __name__ == "__main__":
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = process_lists(list1, list2)
    print(result)
