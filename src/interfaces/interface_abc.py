from abc import ABCMeta, abstractmethod

# Haciendo uso de la metaclase ABC, creamos una interfaz fuertemente tipada
# Donde todas las clases que implementen de esta interfaz tienen que ser una subclase de la interfaz
# Por lo tanto implementaran sus métodos


class IAppService(metaclass=ABCMeta):

    @abstractmethod
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

    # La evaluación siguiente nos dara fallo ya que aunque app_mock tenga el método setup, no es una subclase de
    # IAppService

    # Descomentar para probar
    # assert isinstance(
    #     app_mock, IAppService), f"{app_mock.__class__.__name__} deberia ser una instancia de {IAppService.__name__}"

    # Una manera más fácil de manejar lo anterior sería registrando la clase AppMock
    # como una subclase virtual de IAppService
    IAppService.register(AppMock)

    app_mock_2 = AppMock()

    assert isinstance(
        app_mock_2, IAppService), f"{app_mock_2.__class__.__name__} deberia ser una instancia de {IAppService.__name__}"

    print(isinstance(app_mock_2, IAppService))
