from typing import Protocol, runtime_checkable

# Si hacemos uso de Protocol, hacemos que nuestro código siga una estructura pero tambien sea flexible
# Es decir que podriamos tener una clase que no sea una subclase de Protocol y la interpretaría como tal
# Si al menos unos de sus métodos esta siendo implementado


@runtime_checkable
class IAppService(Protocol):

    def setup(self):
        pass


class AppFrontend(IAppService):
    def setup(self):
        print(f'Init setup {self.__class__.__name__}')


class AppBackend(IAppService):

    def setup(self):
        print(f'Init setup {self.__class__.__name__}')


class AppMock:

    def setup(self):
        print(f'Init setup {self.__class__.__name__}')


if __name__ == '__main__':
    print(issubclass(AppFrontend, IAppService))
    print(issubclass(AppBackend, IAppService))

    app_fronted = AppFrontend()
    app_backend = AppBackend()
    app_mock = AppMock()

    assert isinstance(
        app_mock, IAppService), f"{app_mock.__class__.__name__} deberia ser una instancia de {IAppService.__name__}"

    print(isinstance(app_mock, IAppService))
