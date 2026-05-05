| Technique | Example | Pros | Cons |
|-----------|---------|------|------|
| **Concatenation** (`+`) | `print("Hello, " + name + "! You are " + str(age) + " years old.")` | Simple for beginners | Slow, messy with many variables, requires type conversion |
| **`.format()`** | `print("Hello, {}. You are {} years old.".format(name, age))` | Cleaner than concatenation, works in older Python | Tricky to set up, slower than f-strings |
| **f-strings** (`f""`) | `print(f"Hello, {name}! You are {age} years old.")` | Fastest, cleanest, supports inline expressions | Requires Python 3.6+ |

### **Why Use f-strings?**
✅ **Faster** – Optimized for performance.
✅ **Cleaner** – Less typing, easier to read and set up.
✅ **More powerful** – Supports expressions inside `{}` (e.g., `f"{x * 2}"`).
✅ **Modern standard** – Preferred in Python 3.6+.

Use **f-strings** unless you need backward compatibility with older versions of Python.
