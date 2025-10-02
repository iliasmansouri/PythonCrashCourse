from dataclasses import dataclass
from typing import List


# -------------------------
# Basic class: Animal
# -------------------------
class Animal:
    species = "Unknown"  # class attribute shared by all animals of this class

    def __init__(self, name: str, sound: str = ""):
        """Initializer: set instance attributes."""
        self.name = name
        self.sound = sound

    def speak(self) -> str:
        """Instance method: returns what the animal 'says'."""
        return f"{self.name} says {self.sound}"

    def __str__(self) -> str:
        """Readable string representation (used by print())."""
        return f"{self.__class__.__name__}(name={self.name}, species={self.species})"

    @classmethod
    def from_dict(cls, d: dict):
        """Alternative constructor: create an Animal from a dict."""
        return cls(d.get("name", "Unknown"), d.get("sound", ""))

    @staticmethod
    def is_animal(obj) -> bool:
        """Utility that checks if object looks like an Animal (duck-typing)."""
        return hasattr(obj, "speak") and callable(getattr(obj, "speak"))


# Instantiate and use
dog = Animal("Buddy", "woof")
print(dog.speak())  # Buddy says woof
print("Printable:", dog)  # uses __str__


# -------------------------
# Inheritance: Dog extends Animal
# -------------------------
class Dog(Animal):
    species = "Canis familiaris"  # override class attribute

    def __init__(self, name: str, sound: str = "woof", breed: str = "Unknown"):
        # call parent initializer to reuse setup
        super().__init__(name, sound)
        self.breed = breed

    # new behavior
    def fetch(self, item: str) -> str:
        return f"{self.name} fetched the {item}!"

    # override speak (polymorphism)
    def speak(self) -> str:
        base = super().speak()
        return base + " (happy tail wag!)"

    def __str__(self) -> str:
        # include breed in the printable representation
        return f"Dog(name={self.name}, breed={self.breed})"


mydog = Dog("Rex", "arf", breed="Beagle")
print(mydog.speak())
print(mydog.fetch("ball"))
print("Is mydog an Animal?", Animal.is_animal(mydog))


# -------------------------
# Composition: Zoo contains Animals
# -------------------------
class Zoo:
    """A small container that holds animals (composition example)."""

    def __init__(self, name: str):
        self.name = name
        self._animals: List[Animal] = []

    def add(self, animal: Animal):
        if not Animal.is_animal(animal):
            raise TypeError("Can only add Animal-like objects")
        self._animals.append(animal)

    def all_sounds(self):
        """Return list of speak() results for each animal."""
        return [a.speak() for a in self._animals]

    def __str__(self):
        return f"Zoo({self.name}) with {len(self._animals)} animals"


z = Zoo("Mini Zoo")
z.add(dog)
z.add(mydog)
print(z)
print("Zoo sounds:", z.all_sounds())


# -------------------------
# Dataclass example (concise model)
# -------------------------
@dataclass
class Person:
    name: str
    age: int = 0

    def greet(self) -> str:
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


p = Person("Alex", age=30)
print(p.greet())
print("Dataclass repr:", p)  # nice default __repr__ from dataclass


# -------------------------
# Property example (computed attribute)
# -------------------------
class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def diameter(self) -> float:
        return self.radius * 2

    @diameter.setter
    def diameter(self, value: float):
        # allow setting diameter to update radius
        self.radius = value / 2


c = Circle(3)
print("radius:", c.radius, "diameter:", c.diameter)
c.diameter = 10
print("after setting diameter to 10 -> radius:", c.radius)


# -------------------------
# Small demonstration of "duck typing" (polymorphism)
# -------------------------
class Robot:
    def __init__(self, id_):
        self.id = id_

    def speak(self):
        return f"Robot-{self.id} beep boop"


r = Robot(7)
# both Animal and Robot have a speak() method — we can treat them similarly
for speaker in (dog, mydog, r):
    print("Speaker says:", speaker.speak())


print("\nEnd of OOP demo. Next file: file_IO.py")
