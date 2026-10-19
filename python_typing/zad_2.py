'''Stworzyć funkcję, która przyjmie 2 argumenty typu int, a następnie zwróci wynik mnożenia obu liczb.'''

def multiply(a: int, b: int) -> int:
    return a * b

if __name__ == "__main__":
    num1 = 5
    num2 = 10
    result = multiply(num1, num2)
    print(result)