## Introduction to Python Variables and F-Strings: Station Rotation

### 📋 Rotation Overview

* **Total Time:** 24 minutes of active working time ($3 \text{ stations} \times 8 \text{ minutes}$).
* **Target Audience:** 11th & 12th Graders (Beginner level).
* **Global GitHub Rule:** Save your work to your project folder on your laptop and then upload your work to a GitHub repository named **`variables-station-rotation`** before moving on to the next station.

---

### 📦 Station 1: Naming Variables in Python 
* **Station Format:** Partners
* **Estimated Time:** 8 minutes
* **Learning Objective:** Students will be able to distinguish between legal and illegal Python variable names based on Python's syntax rules.
* **Materials:** A set of printed "Variable Cards" (or a shared digital markdown file), poster paper, and markers.
* **Activity:**
1. Working with your partner, look at the list of 10 Python variable names provided at the station (e.g., `user_age`, `2total`, `player Account`, `class$`, `favorite_color`).
2. Sort the variables into two categories on your poster paper: **"Legal Code"** (Valid names) and **"Syntax Jail"** (Invalid names).
3. For every variable you place in "Syntax Jail," write a brief one-sentence explanation of *why* it broke the rules (e.g., "Started with a number," "Contains a space," "Uses a forbidden symbol").
4. Pick your favorite legal variable name and rewrite it using Python's *snake_case* standard if it isn't already.
5. *Snap a quick photo of your finished poster and save it to your device to upload later.*



---

### 🖥️ Station 2: The Box & Label Analogy (Online)

* **Station Format:** Individual Activity
* **Estimated Time:** 8 minutes
* **Learning Objective:** Students will understand that variables act as labeled storage boxes that hold data values using Python's assignment operator (`=`).
* **Materials:** Laptops, Git/GitHub access, VS Code (or a simple text editor).
* **Activity:**
1. Imagine three empty cardboard boxes. Floating next to them are three data values: `"Alex"`, `17`, and `"Tacos"`.
2. Open your local **`variables-station-rotation`** repository folder in your text editor.
3. Create a new file named `box_analogy.txt` or `box_analogy.md`.
4. Inside this file, virtually "label" your boxes by typing out the exact Python code required to assign those data values to proper variable names.


> **Remember:** In Python, the variable name *always* goes on the left, and the value *always* goes on the right of the `=` sign!


5. Your file should look something like this:
* `box_1_label = "value"`


6. Save the file, commit the changes with the message `"Add box analogy answers"`, and push it to your **`variables-station-rotation`** GitHub repo.



---

### 💻 Station 3: The Storyteller F-String Script (Online)

* **Station Format:** Partner Activity
* **Estimated Time:** 8 minutes
* **Learning Objective:** Students will write a Python script using `print()` and f-strings to inject variables dynamically into a sentence.
* **Materials:** Laptops with Visual Studio Code and Git configured.
* **Activity:**
1. Together with your partner, open your local **`variables-station-rotation`** repository folder in VS Code.
2. Create a new Python file named `madlibs.py`.
3. At the top of the file, declare three variables and assign them values:
* `hero_name` (a string, e.g., `"Jordan"`)
* `item_count` (an integer, e.g., `5`)
* `superpower` (a string, e.g., `"teleportation"`)


4. Below your variables, use the `print()` function combined with an **f-string** to output a short story using those variables. Your code should follow this structure:
```python
print(f"{hero_name} saved the day using {superpower} to move {item_count} boxes!")

```


5. Run your code in the terminal to ensure it works without errors. Take turns changing the variable values to see the story dynamically update!
6. Save your file. Stage, commit your code with the message `"Complete madlibs script"`, and push it up to your **`variables-station-rotation`** GitHub repository.
