# Python String Operations Station Rotation Activity

## Overview

This **35-minute station rotation** focuses on **concatenation** and the **`format()` method** in Python. Students rotate through four stations, alternating between hands-on coding and debugging challenges.

---

## Station Rotation Schedule

| Station       | Activity Type   | Time  | Focus                       |
| ------------- | --------------- | ----- | --------------------------- |
| **Station 1** | Hands-On Coding | 8 min | String Concatenation Basics |
| **Station 2** | Debugging       | 7 min | Fix Concatenation Errors    |
| **Station 3** | Hands-On Coding | 8 min | format() Method Mastery     |
| **Station 4** | Debugging       | 7 min | Fix format() Problems       |

---

## Station 1: String Concatenation Basics

### Objective

Write Python code that uses **concatenation** to build output strings from variables.

### Instructions

Complete the following coding exercises:

1. **Basic Greeting**
    - Create variables: `first_name = "Alex"` and `last_name = "Chen"`
    - Use concatenation to print: `Hello, Alex Chen!`

2. **Math Problem Builder**
    - Create variables: `num1 = 15`, `num2 = 8`
    - Use concatenation to print: `15 + 8 = 23`
    - (Calculate the sum and include it in the output)

3. **Mad Libs Style**
    - Create variables: `adjective = "sparkly"`, `noun = "dragon"`, `verb = "danced"`
    - Use concatenation to print: `The sparkly dragon danced its way across the night sky.`

4. **Color Palette Display**
    - Create a list: `colors = ["red", "blue", "yellow"]`
    - Use concatenation to print each color on a new line with a numbered label:
        ```
        Color 1: red
        Color 2: blue
        Color 3: yellow
        ```

---

## Station 2: Debugging – Concatenation Errors

### Objective

Identify and correct any **concatenation mistakes** in the following code snippets.

### Instructions

Each code snippet has 1-2 errors. Identify the problem, explain what's wrong, and then write the corrected version of the code.

#### Bug #1

```python
name = "Jamie"
age = 16
print("My name is " + name + " and I am " + age + " years old.")
```

**Error:** **\*\*\*\***\_\_\_\_**\*\*\*\***
**Fixed Code:**

```python

```

#### Bug #2

```python
city = "Portland"
state = "Oregon"
result = city + ", " state
print(result)
```

**Error:** **\*\*\*\***\_\_\_\_**\*\*\*\***
**Fixed Code:**

```python

```

#### Bug #3

```python
price = 19.99
item = "notebook"
output = "The " + item + " costs $" + price
print(output)
```

**Error:** **\*\*\*\***\_\_\_\_**\*\*\*\***
**Fixed Code:**

```python

```

#### Bug #4

```python
greeting = "Hello"
name = "Morgan"
message = greeting + " " + name
print(message + "!")
```

**Is this code correct?** YES / NO
**Explanation:** **\*\*\*\***\_\_\_\_**\*\*\*\***

---

## Station 3: String Formatting with format()

### Objective

Use the **`format()` method** to build strings with placeholders and variable insertion.

### Instructions

Complete the following coding exercises using the `format()` method:

1. **Basic Substitution**
    - Create variables: `product = "laptop"`, `brand = "TechPro"`
    - Use `format()` to print: `I own a TechPro laptop.`
    - Code:

        ```python

        ```

2. **Multiple Placeholders**
    - Create variables: `city = "Seattle"`, `population = 750000`, `country = "USA"`
    - Use `format()` to print: `Seattle, USA has a population of 750000.`
    - Code:

        ```python

        ```

3. **Formatting Numbers**
    - Create variables: `item = "coffee"`, `cost = 4.756`
    - Use `format()` to print: `A coffee costs $4.76` (round to 2 decimal places)
    - Code (Hint: use `{:.2f}`):

        ```python

        ```

4. **Sentence Builder with format()**
    - Create variables: `verb = "running"`, `location = "the park"`, `time = "morning"`
    - Use `format()` to print: `I love running in the park during the morning.`
    - Code:

        ```python

        ```

5. **Challenge: Repeating Placeholders**
    - Create a variable: `word = "echo"`
    - Use `format()` to print: `echo echo echo echo echo`
    - (Hint: You can reuse the same placeholder multiple times)
    - Code:

        ```python

        ```

---

## Station 4: Debugging – format() Method Errors

### Objective

Identify and fix **`format()` method mistakes** in the following code snippets.

### Instructions

Each code snippet has 1-2 errors. Identify the problem, explain what's wrong, and write the corrected version.

#### Bug #1

```python
item = "phone"
price = 599.99
print("The {} costs ${}".format(price, item))
```

**Error:** **\*\*\*\***\_\_\_\_**\*\*\*\***
**Fixed Code:**

```python

```

#### Bug #2

```python
name = "Taylor"
age = 14
message = "My name is {} and I am {} years old.format(name, age)"
print(message)
```

**Error:** **\*\*\*\***\_\_\_\_**\*\*\*\***
**Fixed Code:**

```python

```

#### Bug #3

```python
temperature = 72.5
print("The temperature is {:.1f} degrees.".format(temperature))
```

**Is this code correct?** YES / NO
**Explanation:** **\*\*\*\***\_\_\_\_**\*\*\*\***

#### Bug #4

```python
first = "Hello"
second = "World"
result = "{} {}".format(first)
print(result)
```

**Error:** **\*\*\*\***\_\_\_\_**\*\*\*\***
**Fixed Code:**

```python

```

#### Bug #5

```python
student = "Alex"
grade = "A+"
print("Student: {} | Grade: {}".format(student, grade))
```

**Is this code correct?** YES / NO
**Explanation:** **\*\*\*\***\_\_\_\_**\*\*\*\***

---

## Hands-On Coding Rubric

Use this rubric to **self-check your code** at Stations 1 and 3.

| Criteria                        | Excellent (3 pts)                                                                                  | Good (2 pts)                                                                                  | Needs Work (1 pt)                                                                   | Missing (0 pts)                                                                 |
| ------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Correct Syntax**              | Code runs without errors. Proper use of quotes, operators, and method calls.                       | Code runs with minor issues or has 1 small syntax error that's easy to spot.                  | Code has multiple syntax errors but shows understanding of the concept.             | Code does not run or has severe syntax errors.                                  |
| **Proper String Method**        | Uses concatenation (`+`) OR `format()` method correctly and consistently throughout all exercises. | Uses the correct method for most exercises; 1 exercise uses wrong method or has minor misuse. | Uses the correct method but implementation is unclear or incorrect in 2+ exercises. | Does not attempt to use the correct method or uses entirely different approach. |
| **Output Matches Requirements** | Output exactly matches the required format shown in instructions for all exercises.                | Output matches requirements for 3 out of 4+ exercises.                                        | Output matches requirements for 2 out of 4+ exercises.                              | Output does not match requirements or is missing for most exercises.            |
| **Variable Usage**              | All specified variables are correctly created and used in the output strings.                      | Most variables are created and used; 1 variable is missing or unused.                         | Several variables are missing, unused, or incorrectly named.                        | Variables are not used or not created.                                          |
| **Code Clarity**                | Code is easy to read with consistent naming and spacing.                                           | Code is mostly readable; minor spacing or naming issues.                                      | Code is difficult to read due to poor formatting or unclear variable names.         | Code is unorganized or impossible to read.                                      |

---

## Station Transitions & Timing Tips

- **Bell or Signal:** Use a timer or class signal to announce station changes every 7-8 minutes
- **Group Size:** Ideally 7-9 students per station (rotate groups through all 4 stations)
- **Materials:** Have printed copies of all station activities at each location
- **Device Setup:** Ensure students have access to Python (IDLE, Replit, Thonny, or similar)
- **Teacher Role:** Circulate and provide hints; ask guiding questions rather than giving answers

---

## Answer Key (For Teachers)

### Station 1 Sample Answers

**Exercise 1:**

```python
first_name = "Alex"
last_name = "Chen"
print("Hello, " + first_name + " " + last_name + "!")
```

**Exercise 2:**

```python
num1 = 15
num2 = 8
sum_result = num1 + num2
print(str(num1) + " + " + str(num2) + " = " + str(sum_result))
```

**Exercise 3:**

```python
adjective = "sparkly"
noun = "dragon"
verb = "danced"
print("The " + adjective + " " + noun + " " + verb + " across the sky.")
```

**Exercise 4:**

```python
colors = ["red", "blue", "yellow"]
print("Color 1: " + colors[0])
print("Color 2: " + colors[1])
print("Color 3: " + colors[2])
```

### Station 2 Sample Answers

**Bug #1:** Type error – `age` is an integer; must convert to string with `str()`

```python
name = "Jamie"
age = 16
print("My name is " + name + " and I am " + str(age) + " years old.")
```

**Bug #2:** Missing `+` operator between `state` and string

```python
city = "Portland"
state = "Oregon"
result = city + ", " + state
print(result)
```

**Bug #3:** Type error – `price` is a float; must convert to string with `str()`

```python
price = 19.99
item = "notebook"
output = "The " + item + " costs $" + str(price)
print(output)
```

**Bug #4:** YES – This code is correct. Concatenation is used properly.

### Station 3 Sample Answers

**Exercise 1:**

```python
product = "laptop"
brand = "TechPro"
print("I own a {} {}.".format(brand, product))
```

**Exercise 2:**

```python
city = "Seattle"
population = 750000
country = "USA"
print("{}, {} has a population of {}.".format(city, country, population))
```

**Exercise 3:**

```python
item = "coffee"
cost = 4.756
print("A {} costs ${:.2f}".format(item, cost))
```

**Exercise 4:**

```python
verb = "running"
location = "the park"
time = "morning"
print("I love {} in {} during the {}.".format(verb, location, time))
```

**Exercise 5:**

```python
word = "echo"
print("{} {} {} {} {}".format(word, word, word, word, word))
```

### Station 4 Sample Answers

**Bug #1:** Arguments are in wrong order – price and item are swapped

```python
item = "phone"
price = 599.99
print("The {} costs ${:.2f}".format(item, price))
```

**Bug #2:** Missing dot (`.`) before `format` – should be `.format()`

```python
name = "Taylor"
age = 14
message = "My name is {} and I am {} years old.".format(name, age)
print(message)
```

**Bug #3:** YES – This code is correct. The `{:.1f}` format specifier properly rounds to 1 decimal place.

**Bug #4:** Missing second argument – `format()` has only one value but needs two

```python
first = "Hello"
second = "World"
result = "{} {}".format(first, second)
print(result)
```

**Bug #5:** YES – This code is correct. Both placeholders have matching arguments in the correct order.
