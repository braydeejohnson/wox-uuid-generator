import pkgutil
from importlib import import_module
from .Container import IocContainer
from dependency_injector.providers import Singleton, Factory, Object, Callable


class Application:
    def __init__(self):
        self.container = IocContainer()
        self.bootstrap()

    def bootstrap(self):
        self.build_configuration()
        self.register_providers()

    def get_binding(self, alias):
        if hasattr(self.container, alias):
            return getattr(self.container, alias)

    def make(self, alias):
        if hasattr(self.container, alias):
            return getattr(self.container, alias)()

    def singleton(self, alias, instance, *args, **kwargs):
        setattr(self.container, alias, Singleton(instance, *args, **kwargs))

    def object(self, alias, instance):
        setattr(self.container, alias, Object(instance))

    def callable(self, alias, instance, *args, **kwargs):
        setattr(self.container, alias, Callable(instance, *args, **kwargs))

    def factory(self, alias, instance, *args, **kwargs):
        setattr(self.container, alias, Factory(instance, *args, **kwargs))

    def register_providers(self):
        for (_, key, _) in pkgutil.iter_modules(['services/providers']):
            try:
                provider = import_module(f"services.providers.{key}")
                provider.register(self, self.container.config)
            except BaseException as error:
                print("Failed to register provider `{}`".format(key))
                print(error)

    def build_configuration(self):
        configuration = {}
        for (_, key, _) in pkgutil.iter_modules(['config']):
            try:
                config = import_module(f"config.{key}")
                configuration[key] = config.config
            except BaseException as error:
                print("Failed to parse configuration for {}".format(key))
                print(error)

        self.container.config.override(configuration)