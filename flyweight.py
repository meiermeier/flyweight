class Flyweight(type):
    def __init__(cls, *args, **kwargs):
        cls._registry = {}
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        data = (args, tuple(kwargs.items()))

        if not (instance := cls._registry.get(data)):
            instance = cls._registry[data] = super().__call__(*args, **kwargs)

        return instance


if __name__ == '__main__':
    class A(metaclass=Flyweight):

        def __init__(self, a):
            print('init', a)


    A(1)
    A(1)
    A(1)
    A(2)
    A(2)
    A(2)
