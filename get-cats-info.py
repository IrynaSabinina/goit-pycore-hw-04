def get_cats_info(path):
    cats_info = []  # Список для збереження інформації про котів
    try:
        # Відкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Розділяємо рядок на частини: id, name та age
                    cat_id, name, age = line.strip().split(',')
                    # Створюємо словник для кожного кота
                    cat = {
                        'id': cat_id,
                        'name': name,
                        'age': int(age)  # Вік перетворюємо на ціле число
                    }
                    cats_info.append(cat)
                except ValueError:
                    # Якщо рядок не містить правильної кількості елементів
                    print(f"Неправильний формат даних: {line.strip()}")
                    continue

        return cats_info

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

# Приклад використання:
path = 'cats_info.txt'
cats = get_cats_info(path)
print(cats)
