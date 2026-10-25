"""2. Stworzyć następujące klasy:
    - Library (klasa opisująca bibliotekę), posiadająca pola:
        - city
        - street
        - zip_code
        - open_hours (str)
        - phone
    - Employee (klasa opisująca pracownika biblioteki), posiadająca pola:
        - first_name
        - last_name
        - hire_date
        - birth_date
        - city
        - street
        - zip_code
        - phone
    - Book (klasa opisująca książkę), posiadająca pola
        - library
        - publication_date
        - author_name
        - author_surname
        - number_of_pages
    - Order (klasa opisująca zamówienie), posiadająca pola:
        - employee
        - student
        - books (lista obiektów klasy Book)
        - order_date
    
    Dodatkowo:
    
    - Każda klasa ma mieć zaimplementowaną metodę `__str__`, która będzie opisywała obiekt oraz 
    ewentualne obiekty znajdujące się w tym obiekcie (np. obiekt Library w obiekcie Book).
    - Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy 
    za pośrednictwem konstruktora.
    - Stworzyć 2 biblioteki (2 instancje klasy), 5 książek, 3 pracowników, 3 studentów, oraz 2 
    zamówienia.
    - Wyświetlić oba zamówienia (`print`)"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library in {self.city}, {self.street}, {self.zip_code}, Open hours: {self.open_hours}, Phone: {self.phone}"

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, Hired: {self.hire_date}, Born: {self.birth_date}, Address: {self.city}, {self.street}, {self.zip_code}, Phone: {self.phone}"

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book by {self.author_name} {self.author_surname}, Published: {self.publication_date}, Pages: {self.number_of_pages}, Library: {self.library}"

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = ', '.join(str(book) for book in self.books)
        return f"Order by {self.student.name}, Processed by: {self.employee.first_name} {self.employee.last_name}, Books: [{books_str}], Order Date: {self.order_date}"

lib1 = Library("Warszawa", "Marszałkowska", "00-001", "08:00-20:00", "111-222-333")
lib2 = Library("Kraków", "Floriańska", "30-001", "09:00-18:00", "444-555-666")

emp1 = Employee("Anna", "Kowalska", "2020-01-15", "1990-05-20", "Warszawa", "Jasna", "00-100", "123-123-123")
emp2 = Employee("Tomasz", "Nowak", "2021-03-01", "1985-11-11", "Kraków", "Ciemna", "30-200", "321-321-321")
emp3 = Employee("Zofia", "Wiśniewska", "2023-06-10", "1995-02-28", "Warszawa", "Prosta", "00-300", "999-888-777")

student1 = Student("Jan Kowalski", [60, 70, 80])
student2 = Student("Anna Nowak", [40, 30, 20])
student3 = Student("Piotr Wiśniewski", [55, 65, 75])

book1 = Book(lib1, "2020-01-01", "Adam", "Mickiewicz", 300)
book2 = Book(lib1, "2019-05-15", "Juliusz", "Słowacki", 250)
book3 = Book(lib2, "2018-07-20", "Henryk", "Sienkiewicz", 400)
book4 = Book(lib2, "2021-09-10", "Bolesław", "Prus", 350)
book5 = Book(lib1, "2022-11-05", "Maria", "Konopnicka", 200)

order1 = Order(emp1, student1, [book1, book2], "2024-06-01")
order2 = Order(emp2, student2, [book3, book4, book5], "2024-06-02")

print(order1)
print(order2)
