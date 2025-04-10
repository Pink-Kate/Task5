from typing import Callable, Generator
def generator_numbers(text: str) -> Generator[float, None, None]:
    for word in text.split():
        try:
            number = float(word)
            yield number
        except ValueError:
            continue

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return round(sum(func(text)), 2)

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
