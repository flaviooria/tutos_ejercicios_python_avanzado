import functools
from typing import Callable, Any, Literal

Methods = Literal['get', 'post', 'put', 'delete']


# Vamos a crear una función que simule o realize una llamada a una api, donde pintaremos el resultado,
# Esta función tendra que tener un decorador de envoltorio que pinte inciciando petición, mostrando el nombre del
# endpoint

def decorator_with_arguments(endpoint: str):
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f'Execute {func.__name__} calling endpoint {endpoint}')
            func(*args, **kwargs)
            print(f'Finished {func.__name__} finish calling endpoint {endpoint}')

        return wrapper

    return decorator


@decorator_with_arguments('/random')
def call_api(url: str):
    print([f'{url}/{++x}' for x in range(1, 11)])


class ApiRoute:
    def __init__(self, url: str, methods: Methods):
        self.url = url
        self.methods = methods

    def execute(self):
        print(f'Fetch api endpoint {self.url} with method {self.methods}')


class Api:

    def __init__(self):
        self._routes: dict[str, ApiRoute] = {}

    def route(self, endpoint: str, method: Methods = 'get'):
        self._routes[endpoint] = ApiRoute(endpoint, method)

        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            @functools.wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                self._routes[endpoint].execute()
                value = func(*args, **kwargs)
                return value

            return wrapper

        return decorator


app = Api()


@app.route('/users', 'get')
def get_users() -> list[str]:
    return ['Flavio', 'Lau', 'Gabi']


if __name__ == '__main__':
    # call_api('https://random-api.ml')
    print(get_users())
