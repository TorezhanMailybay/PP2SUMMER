class Animal:
    def make_sound(self):
        print("Some sound")

class Dog(Animal):
    def make_sound(self):   # overriding
        print("Woof!")

a = Animal()
d = Dog()

a.make_sound()  # Some sound
d.make_sound()  # Woof!

