Here are two simple examples using a `Dog` class and a `Car` class to help students understand the difference between **class attributes** (shared by all instances) and **instance attributes** (unique to each specific object).

---

## Example 1: The `Dog` Class

This example demonstrates how a class attribute defines a global characteristic for a species, while instance attributes define the unique traits of individual dogs.

```python
class Dog:
    # CLASS ATTRIBUTE: Shared by all instances of the Dog class.
    # Every dog belongs to the same species, regardless of its breed or name.
    species = "Canis lupus"

    def __init__(self, name, breed):
        # INSTANCE ATTRIBUTES: Unique to each specific dog object.
        # Different dogs will have different names and breeds.
        self.name = name
        self.breed = breed


# --- Creating Instances (Objects) ---

# Object 1: Buddy the Golden Retriever
dog1 = Dog("Buddy", "Golden Retriever")

# Object 2: Luna the Labrador
dog2 = Dog("Luna", "Labrador")


# --- Accessing Attributes ---

# 1. Accessing Instance Attributes
# Notice how the output is different for each dog.
print(f"{dog1.name} is a {dog1.breed}.")  # Output: Buddy is a Golden Retriever.
print(f"{dog2.name} is a {dog2.breed}.")  # Output: Luna is a Labrador.

# 2. Accessing the Class Attribute
# Notice how both dogs share the exact same species value.
print(f"{dog1.name}'s species is {dog1.species}.")  # Output: Buddy's species is Canis lupus.
print(f"{dog2.name}'s species is {dog2.species}.")  # Output: Luna's species is Canis lupus.

# You can also access the class attribute directly using the Class name:
print(f"All dogs belong to the species: {Dog.species}")  # Output: Canis lupus

```

---

## Example 2: The `Car` Class

This example shows how a class attribute can act as a universal constant or counter (like the number of wheels), while instance attributes describe the specific details of a particular vehicle.

```python
class Car:
    # CLASS ATTRIBUTE: Shared by all cars.
    # Standard cars universally have 4 wheels.
    number_of_wheels = 4

    def __init__(self, make, model, color):
        # INSTANCE ATTRIBUTES: Unique to each specific car object.
        # Cars on the road have different makers, models, and paint jobs.
        self.make = make
        self.model = model
        self.color = color


# --- Creating Instances (Objects) ---

# Object 1: A red Tesla
car1 = Car("Tesla", "Model 3", "Red")

# Object 2: A blue Ford
car2 = Car("Ford", "Mustang", "Blue")


# --- Accessing Attributes ---

# 1. Accessing Instance Attributes
# The details change depending on which specific car we are looking at.
print(f"Car 1 is a {car1.color} {car1.make} {car1.model}.")  # Output: Car 1 is a Red Tesla Model 3.
print(f"Car 2 is a {car2.color} {car2.make} {car2.model}.")  # Output: Car 2 is a Blue Ford Mustang.

# 2. Accessing the Class Attribute
# Even though they are completely different models, they share the same number of wheels.
print(f"The {car1.model} has {car1.number_of_wheels} wheels.")  # Output: The Model 3 has 4 wheels.
print(f"The {car2.model} has {car2.number_of_wheels} wheels.")  # Output: The Mustang has 4 wheels.

```

---

### Key Takeaways:

* **Class Attributes:** Defined directly inside the class body (outside of any methods). They are useful for storing data that should be identical across **all** objects of that type.
* **Instance Attributes:** Defined inside the `__init__` method using the `self` keyword. They are used to store data that distinguishes one object from another.