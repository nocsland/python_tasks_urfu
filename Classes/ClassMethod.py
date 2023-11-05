class ParentClass:
    @classmethod
    def method(cls, arg):
        print(print("%s classmethod. %d" % (cls.__name__, arg)))

    @classmethod
    def call_original_method(cls):
        cls.method(5)

    def call_class_method(self):
        self.method(10)


class ChildClass(ParentClass):
    @classmethod
    def call_original_method(cls):
        cls.method(6)


# Вызываем методы класса через класс.
ParentClass.method(0)
ParentClass.call_original_method()

ChildClass.method(0)
ChildClass.call_original_method()

# Вызываем методы класса через объект.
my_obj = ParentClass()
my_obj.method(1)
my_obj.call_class_method()
