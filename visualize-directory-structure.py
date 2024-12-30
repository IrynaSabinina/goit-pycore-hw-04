import os
import sys
from pathlib import Path
from colorama import Fore, init

# Ініціалізація colorama
init(autoreset=True)

def visualize_directory_structure(path):
    # Перевірка на існування та коректність шляху
    directory = Path(path)
    if not directory.exists():
        print(Fore.RED + f"Помилка: шлях '{path}' не існує!")
        return
    if not directory.is_dir():
        print(Fore.RED + f"Помилка: '{path}' не є директорією!")
        return

    # Функція для рекурсивного виведення структури директорії
    def print_directory_contents(directory, indent=""):
        for item in directory.iterdir():
            if item.is_dir():
                print(Fore.BLUE + indent + f"[Директорія] {item.name}")
                print_directory_contents(item, indent + "  ")  
            elif item.is_file():
                print(Fore.GREEN + indent + f"[Файл] {item.name}")

    # Початкова виведення структури
    print_directory_contents(directory)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Будь ласка, вкажіть шлях до директорії.")
        sys.exit(1)

   
    # path = sys.argv[1]
    # visualize_directory_structure(path)
