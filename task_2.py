text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

import re

def generator_numbers(text):
    pattern = r'(?<!\S)(-?\d+(\.\d+)?)(?!\S)'  # Регулярний вираз для пошуку дійсних чисел, які чітко відокремленні пробілами
    
    for match in re.finditer(pattern, text):   # Цикл який проходить по тесту і число 
        yield float(match.group(0))            # Повертає та запам'ятовує значення першого входження та конвертує із строки в дійсне число


def sum_profit(text, func):
    return sum(func(text))  

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")