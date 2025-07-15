# Inheritance Example

class Animal:
    def speak(self):
        print("I am an animal.")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.speak()
dog.bark()