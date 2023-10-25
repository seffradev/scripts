from typing import Generator
import sys

def factors(number: int) -> Generator[int, None, None]:
    """Return a list of factors of a given number."""
    return (i for i in range(1, number // 2 + 1) if number % i == 0)

def sociable(number: int) -> int:
    """Return the sociable number of a given number."""
    return sum(factors(number))

def is_sociable(original_number: int, max_tries: int = 5) -> bool:
    """Return True if a given number is sociable."""
    number = original_number
    for _ in range(max_tries):
        number = sociable(number)
        if number == original_number:
            return True
    return False

if __name__ == '__main__':
    max_tries = 5

    try:
        number = int(sys.argv[1])

        if len(sys.argv) > 2:
            max_tries = int(sys.argv[2])
    except ValueError:
        print("Please enter a valid number.")
        exit(1)
    except IndexError:
        print("Not enough arguments were provided.")
        exit(1)

    if is_sociable(number, max_tries):
        print("sociable")
    else:
        print("not sociable")
