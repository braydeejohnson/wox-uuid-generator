from dependency_injector.providers import Configuration
from dependency_injector.containers import DeclarativeContainer


class IocContainer(DeclarativeContainer):
    """
    IOC Container for Dependency Injection for reusable services
    """
    config = Configuration('config')