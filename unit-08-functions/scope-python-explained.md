# Understanding Variable Scope in Python

## What is Variable Scope?

**Variable scope** is the region or area of your code where a variable can be accessed and used. Think of it like a library system: a book checked out from the reference section can only be used in the library, while a book you take home is available in your house. Similarly, variables exist in different "zones" in your code, and you can only use them in certain places.

---

## Why Does Scope Matter?

Imagine you're organizing a school project and each group member has their own folder with notes. You wouldn't expect to access another group's private notes without permission, right? The same idea applies to variables:

- **Organization**: Scope helps keep variables organized and prevents confusion
- **Safety**: Variables can't be accidentally changed by code that shouldn't access them
- **Clarity**: Knowing where a variable exists makes code easier to understand

---

## The Four Main Types of Scope

### Global Scope

A **global variable** is created at the top level of your program and can be accessed anywhere in your code.

```python
message = "Hello, everyone!"  # Global variable

def greet():
    print(message)  # Can use global variable here

greet()  # Output: Hello, everyone!
print(message)  # Can also use it here
```

**Key point**: Global variables are accessible everywhere, but you should use them sparingly because it can make code confusing.

### Local Scope

A **local variable** is created inside a function and only exists within that function.

```python
def say_goodbye():
    farewell = "See you later!"  # Local variable
    print(farewell)  # Works fine here

say_goodbye()  # Output: See you later!
print(farewell)  # ERROR! farewell doesn't exist outside the function
```

**Key point**: Once the function finishes running, the local variable disappears.

### Enclosing Scope (Nested Functions)

When you have a function inside another function, the inner function can access variables from the outer function.

```python
def outer_function():
    outer_var = "I'm from the outer function"  # Enclosing scope

    def inner_function():
        print(outer_var)  # Can access outer_var here

    inner_function()  # Output: I'm from the outer function

outer_function()
```

**Key point**: The inner function can "see" variables from the outer function, but not the other way around.

### Built-in Scope

**Built-in scope** includes functions and variables that Python provides automatically, like `print()`, `len()`, and `range()`. These are available everywhere without you having to define them.

```python
print(len([1, 2, 3]))  # print() and len() are built-in
# Output: 3
```

---

## The LEGB Rule

Python looks for variables in this order: **Local → Enclosing → Global → Built-in** (LEGB). This is like searching your desk, then your room, then your house, then asking your neighbors.

```python
x = "I'm global"  # Global

def outer():
    x = "I'm enclosing"  # Enclosing

    def inner():
        x = "I'm local"  # Local
        print(x)  # Prints: I'm local

    inner()

inner()  # ERROR - inner() doesn't exist here
outer()  # Output: I'm local
```

---

## Common Scope Problems and How to Avoid Them

### Problem 1: Forgetting Variables Are Local

```python
count = 0  # Global

def add_one():
    count = count + 1  # ERROR! Trying to use count before setting it locally
    return count

add_one()
```

**Solution**: If you want to modify a global variable inside a function, use the `global` keyword:

```python
count = 0  # Global

def add_one():
    global count  # Tell Python to use the global count
    count = count + 1
    return count

add_one()  # Works! count is now 1
```

### Problem 2: Confusing Variable Names

```python
name = "Alice"  # Global

def print_name():
    name = "Bob"  # Local variable with same name
    print(name)  # Prints: Bob (the local one)

print_name()  # Output: Bob
print(name)  # Output: Alice (the global one unchanged)
```

**Solution**: Use clear, descriptive variable names so it's obvious which version you're using.

---

## Quick Reference: Scope Cheat Sheet

| Scope Type    | Created Where                               | Can Access                 |
| ------------- | ------------------------------------------- | -------------------------- |
| **Local**     | Inside a function                           | Only inside that function  |
| **Enclosing** | In an outer function (for nested functions) | Only in the inner function |
| **Global**    | At the top level of your program            | Anywhere in your code      |
| **Built-in**  | Python provides it automatically            | Anywhere in your code      |

---

## Practice Questions

1. **What's the difference between a global and local variable?**
2. **If you create a variable inside a function, can you use it outside the function?**
3. **What does the `global` keyword do?**
4. **In the LEGB rule, which scope is checked first?**

---

## Key Takeaways

✓ **Scope determines where a variable can be used**

✓ **Local variables are created in functions and only exist there**

✓ **Global variables exist everywhere but should be used carefully**

✓ **Python searches for variables in this order: Local → Enclosing → Global → Built-in**

✓ **Understanding scope helps prevent bugs and makes your code easier to follow and understand**
