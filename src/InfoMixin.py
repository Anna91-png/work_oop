class InfoMixin:
    def __init__(self, *args, **kwargs):
        print(f"[INFO] Создан объект класса {self.__class__.__name__} с параметрами: {args} {kwargs}")
        super().__init__(*args, **kwargs)
