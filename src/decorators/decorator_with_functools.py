import logging
import time
from typing import Callable, Any
import functools


def is_divisible_by_3(number: int) -> bool:
    return number % 3 == 0


# El uso de functools.wraps sirve para envolver la función y actualizar con ella los metadatos de la función envuelta
# De esta manera si llamamos el nombre de la función que estamos ejecutando se llamaría a la función que se esta
# decorando y no a la wrapped


# Decorador que utilizaremos para ver la performance de la función
def benchmark(func: Callable[[int], int]) -> Callable[[...], Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time

        logging.info(f'Function {func.__name__} took {total_time} seconds')

        return result

    return wrapper


def logger(func: Callable[[int], Any]) -> Callable[[...], Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        logging.basicConfig(level=logging.INFO)
        logging.info(f'{func.__name__} started')
        result = func(*args, **kwargs)
        logging.info(f'Number total divisible by 3 is: {result}')
        logging.info(f'{func.__name__} finished')

    return wrapper


@logger
@benchmark
def count_numbers_divisible_by_3(number: int) -> int:
    count: int = 0

    for div in range(1, number + 1):
        if not is_divisible_by_3(div):
            continue

        count += 1

    return count


def main():
    count_numbers_divisible_by_3(9500)


if __name__ == '__main__':
    main()
