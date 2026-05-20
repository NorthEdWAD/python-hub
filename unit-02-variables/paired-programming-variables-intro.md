# Python: Working with Variables & Python f-Strings
## Paired Programming Activity

**Goal:** Learn how to correctly name Python variables, assign a value to a variable, and use f-strings inside the `print()` function to display the value that was assigned to a variable.

---

### Roles

* **Pilot:** Controls the keyboard and mouse. Your job is to type the code exactly as agreed upon and focus on correct syntax.
* **Navigator:** Keeps their eyes on this sheet and the screen. Your job is to catch typos, ensure variable naming rules are followed, and guide the pilot as s/he writes the code.

> **NOTE:** You will switch roles halfway through!

---

### Tasks

#### Part 1: Strict Naming & Assignment (10 Minutes) - *Pilot 1 & Navigator 1*

Python has strict rules for variables. They must start with a letter or underscore, can only contain letters, numbers, and underscores (`_`), and are case-sensitive. They should also use **snake_case** (all lowercase, words separated by underscores).

1. **Create a valid string variable:** Create a variable named `player_name` and assign it the name of your favorite video game or movie character.
2. **Create a valid integer variable:** Create a variable named `player_score` and assign it a whole number greater than 1000.
3. **Test the rules:** Try to create a variable named `1st_place` and assign it a value. Look at the error Python gives you.
4. **Fix it:** Change `1st_place` to a valid Python variable name.  What change would you have to make to do this?

#### Part 2: The F-String Reveal (10 Minutes) - *Switch Roles Now!*

An f-string lets you insert variables directly into a sentence by placing an `f` in front of the quotation marks and putting the variable inside curly braces `{}`.

5. **Basic Print:** Use a standard `print()` function to display a simple "Hello World" message to ensure your console works.
6. **The F-String:** Write a single `print()` statement using an f-string that displays the player's name and score in a full sentence.
* *Example format:* `print(f"Welcome back, {variable_one}! Your current score is {variable_two}.")`


7. **Add Calculation:** Create a new variable called `bonus_points` and set it to `500`. Write a new f-string `print()` statement that displays their new total score by adding the two score variables together inside the curly braces.

---

### Discussion Questions

* **Syntax Check:** Why does Python reject a variable name like `player score` (with a space) or `1st_place`? What rule did those break?
* **The Power of F-Strings:** How do f-strings make your `print()` statements easier to read and write compared to smashing text and variables together with commas or plus signs?
