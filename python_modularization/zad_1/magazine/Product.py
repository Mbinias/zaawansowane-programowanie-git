# Import niezależny (absolutny) zaczynający się od nazwy głównego pakietu
import magazine.utils


class Product:
    def __init__(self):
        print("Product...")
        magazine.utils.help_func()
