# =====================================================================
# CHALLENGE: Find and correct the TWO errors hidden in each section!
# =====================================================================

# --- SECTION 1: DOG ---
class dog
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"

# Testing Section 1
dog1 = Dog("Rover")
print(dog1.bark())


# --- SECTION 2: CAT ---
class SiameseCat:
    def __init__(self, name, color):
        self.name = name
        self.color == color

    def meow(self):
        print(f"{self.name} meows softly.")

# Testing Section 2
cat1 = SiameseCat("Luna")
cat1.meow()


# --- SECTION 3: CAR ---
class ElectricCar:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self)
        return f"The {self.make} {self.model} silently drives away."

# Testing Section 3
car1 = ElectricVehicle("Tesla", "Model 3")
print(car1.drive())


# --- SECTION 4: BOOK ---
class AudioBook:
    def __init__(self, title, author):
        title = title
        self.author = author

    def play(self):
        return f"Playing {self.title} by {self.author}."

# Testing Section 4
book1 = AudioBook("The Hobbit", "J.R.R. Tolkien")
print(book1.play())