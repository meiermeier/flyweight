import weakref

class Flyweight(type):
    def __init__(cls, *args, **kwargs):
        cls._pool = weakref.WeakValueDictionary()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        data = (args, tuple(kwargs.items()))

        instance = cls._pool.get(data)
        if not instance:
            instance = cls._pool[data] = super().__call__(*args, **kwargs)
            
        return instance
