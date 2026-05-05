# Python f-strings vs t-strings: A Quick Guide

## What are f-strings?
F-strings (formatted string literals) are a Python feature introduced in 3.6 for string interpolation. They are prefixed with `f` and allow expressions inside curly braces `{}`.

```python
name = "Alice"
age = 30
print(f"{name} is {age} years old.")
# Output: Alice is 30 years old.
```

## What are t-strings?
T-strings (template strings) are a simpler alternative using the `str.format()` method. They use curly braces `{}` but are called with `.format()`.

```python
name = "Bob"
age = 25
print("{name} is {age} years old.".format(name=name, age=age))
# Output: Bob is 25 years old.
```

## Key Differences

| Feature       | f-strings                          | t-strings                          |
|--------------|-----------------------------------|-----------------------------------|
| Syntax       | `f"..."`                          | `"...".format(...)`               |
| Readability  | More concise                      | More verbose                      |
| Performance  | Faster (compiled at runtime)      | Slower (method call overhead)     |
| Python Version | Requires 3.6+                   | Works in older versions           |
| Expressions  | Supports inline expressions       | Requires separate variables       |

## Advantages of t-strings
- **Backward compatibility**: Works in Python 2.7+ and 3.x.
- **Explicit variable binding**: Clearer when variables are reused.

## Disadvantages of t-strings
- **Verbose**: Requires `.format()` calls.
- **Slower**: Method call overhead reduces performance.
- **No inline expressions**: Cannot embed logic directly.

## When to Use Which?
- **Use f-strings** for modern Python (3.6+) for cleaner, faster code.
- **Use t-strings** for compatibility with older Python versions or when explicit formatting is preferred.

```python
# Prefer f-strings in modern code:
print(f"{name} is {age} years old.")

# Use t-strings for compatibility:
print("{name} is {age} years old.".format(name=name, age=age))
```