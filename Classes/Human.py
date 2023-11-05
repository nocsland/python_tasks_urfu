class Human:
    age = None

    def __init__(self, age=4):
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age > 0 and isinstance(age, int):
            self.age = age


human = Human()
human.set_age(5)
print(human.get_age())
