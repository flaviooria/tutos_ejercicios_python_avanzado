# Decoradores con argumento
import functools
import logging
from typing import Any, Callable

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('Decorador con argumentos')


def decorator_with_arguments(log: logging.Logger):
    def decorator(func: Callable[..., int]) -> Callable[[...], Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            log.info(f'Calling {func.__name__}')
            log.info(f'Init {func.__name__}')
            value = func(*args, **kwargs)
            log.info(f'Result of function {func.__name__} is: {value}')
            log.info(f'Finished {func.__name__}')

        return wrapper

    return decorator


def is_divisible_by_3(number: int) -> bool:
    return number % 3 == 0


@decorator_with_arguments(logger)
def count_numbers_divisible_by_3(number: int) -> int:
    count: int = 0

    for div in range(1, number + 1):
        if not is_divisible_by_3(div):
            continue

        count += 1

    return count


def main():
    count_numbers_divisible_by_3(9515)


if __name__ == '__main__':
    main()
