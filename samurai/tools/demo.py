class SingletonMeta(type):
    """自定义单例元类"""

    def __init__(cls, *args, **kwargs):
        print("__init__")
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print("__call__")
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    pass


if __name__ == '__main__':
    president = President()
    print(president)
    presiden = President()
    print(presiden)