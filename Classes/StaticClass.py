class StaticClass:
    @staticmethod
    def bar():
        """Вывод данных"""
        print("bar")


# Вызов статического метода через класс считается плохим тоном
obj = StaticClass()
obj.bar()


class StaticClass2:

    @staticmethod
    def get_bar():
        """Вернуть данные"""
        return "bar"


# Правильно вызывать статический метод так:
print(StaticClass2.get_bar())
