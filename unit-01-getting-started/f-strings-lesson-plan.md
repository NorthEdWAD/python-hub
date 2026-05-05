## **📅 Monday: Focus on What Matters**

### **Activities**
- Identify 3–4 core concepts: f-string syntax, variable interpolation, and comparing output methods (concatenation/`.format()`)
- Plan one main activity: "The Bio Generator" (creating strings from user data)
- Remove non-essential materials: Advanced formatting (padding, precision) to keep focus on basic output

### **Handouts & Files**
- **📄 Core Objectives Worksheet**: Mastery of `f"Text {variable}"`
- **🗑️ "Cut List"**: Remove complex string slicing or nested formatting

---

## **📅 Tuesday: Build the Lesson**

### **Explanation: The Evolution of Strings**
Before **f-strings**, Python users had to "glue" strings together or use placeholders:
* **Concatenation**: Using `+` to join strings (e.g., `"Hello " + name`). It's manual and requires converting numbers to strings.
* **The `.format()` Method**: Using `{}` as placeholders (e.g., `"Hello {}".format(name)`). Better, but wordy.
* **f-strings**: The modern way. Just put an `f` before the quotes and variables inside `{}`.

### **Activities**
- Draft lesson steps: Demonstrate the "old ways" vs. the "f-string way"
- Design activity: **"The Hero Stats Card"**—students create variables for a character (name, health, power) and print a summary
- Review for technical clarity: Ensure students understand that `f` must be outside the quote marks

### **Handouts & Files**
- **📝 Lesson Plan Outline**: Comparison chart of output methods
- **💻 Starter Template**: Variables like `user = "Player1"` and `score = 10`
- **🎯 Hands-On Activity Sheet**: "Hero Stats Card" instructions

---

## **📅 Wednesday: Gather the Best Resources**

### **Activities**
- Find one high-quality tutorial: "Python f-strings for Beginners"
- Create boilerplate code showing `print(f"Score: {score}")`
- Verify resource functionality: Ensure the Python environment supports version 3.6+ (required for f-strings)

### **Handouts & Files**
- **🎥 Resource Link**: Short video on f-string efficiency
- **💻 Demo File**: `string_styles_demo.py`
- **✅ Testing Checklist**: Check that code runs without `TypeError` during concatenation

---

## **📅 Thursday: Test Understanding**

### **Activities**
- Create a targeted assessment: Fix a broken f-string
- Define a simple rubric: Correct syntax, successful variable placement, and code readability
- Align assessment with Monday's goals: Does the student know when to use `{}`?

### **Handouts & Files**
- **📝 Assessment Sheet**: "Code Doctor"—Debugging f-strings
- **📊 Rubric**: Criteria for clean string output
- **🔍 Validation Notes**: Confirm focus remains on simple variable interpolation

---

## **📅 Friday: Final Touches**

### **Activities**
- Organize final materials into a "Python Strings" unit folder
- Perform final audit: Remove any reference to the `%` formatting (too outdated)
- Save and backup all materials

### **Handouts & Files**
- **📁 Finalized Unit Folder**: All templates and scripts
- **🗑️ Redundancy List**: Deleted complex `%` formatting slides
- **💾 Backup File**: Cloud copy of the "f-string" unit

---

### **Essentialist Assessment Strategies**

| Method | Time | Purpose |
| :--- | :--- | :--- |
| **One-Question Task** | 1–2m | "Write an f-string that prints your name and favorite color." |
| **Live Coding/Demo** | 3–5m | Student updates a `.format()` line into an f-string on the board. |
| **Fist-to-Five** | 1m | "How confident are you with using curly braces `{}`?" |
| **Peer Teaching** | 5m | Explain to a partner why f-strings are easier than concatenation. |
| **Muddiest Point** | 2–3m | "Do I still need to use `str()` inside an f-string?" |
| **Snippet Fix** | 3–5m | Fix: `print("Hello {name}")` (Missing the `f`). |

---

### **Key Takeaway**
* **Focus**: Mastery of f-strings as the primary output method.
* **Speed**: Immediate feedback via short coding bursts.
* **Agency**: Students debug common mistakes (like forgetting the `f`) to build independence.
