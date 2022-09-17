class Dog:
    def walk(self):
        return " walking "

    def speak(self):
        return "Woof Woof !"

class JackTerrier(Dog):
    def talk(self):
        return super().speak() 

spike = JackTerrier()
print(spike.talk())
print(spike.walk())
print(spike.speak())
