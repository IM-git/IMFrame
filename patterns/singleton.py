class Singleton(type):
    """Singleton is a creational design pattern
    that lets you ensure that a class has only one instance,
    while providing a global access point to this instance."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
