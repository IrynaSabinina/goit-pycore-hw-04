def total_salary(path):
    try:
        # Відкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                # Розділяємо рядок на прізвище та зарплату
                try:
                    name, salary = line.strip().split(',')
                    salary = int(salary)  # Конвертуємо зарплату в число
                    total += salary
                    count += 1
                except ValueError:
                    # Якщо рядок не має правильного формату
                    print(f"Неправильний формат даних: {line.strip()}")
                    continue
            
            if count == 0:
                return (0, 0)  # Якщо в файлі немає розробників
            
            # Обчислюємо середню зарплату
            average = total / count
            return (total, average)
    
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return (0, 0)  # Повертаємо нулі, якщо файл не знайдено
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)  # Повертаємо нулі, якщо сталася інша помилка

# Приклад використання:
path = 'developers_salaries.txt'
result = total_salary(path)
print(f"Загальна сума зарплат: {result[0]}, Середня зарплата: {result[1]}")
