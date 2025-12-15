# Chapter 2 — Flow Control

**Disclaimer:** Although these notes were AI-generated, the code in the exercises folder was completed by me. This is solely to create a comprehensive, completed folder for each chapter of *Automate the Boring Stuff with Python*.

These notes cover **Chapter 2 of _Automate the Boring Stuff with Python_**. This chapter teaches Python how to **make decisions and repeat actions**.

---

## What Is Flow Control?
Flow control lets your program:
- **Run code conditionally** (if something is true)
- **Repeat code** (loops)
- **Stop or skip execution** when needed

Without flow control, programs just run top → bottom once.

---

## Boolean Values
Booleans represent **truth values**:

```python
True
False
```

They are the backbone of decision-making.

---

## Comparison Operators
Used to compare values. They return `True` or `False`.

| Operator | Meaning | Example | Result |
|--------|--------|--------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less or equal | `5 <= 5` | `True` |
| `>=` | Greater or equal | `6 >= 5` | `True` |

⚠️ `=` is **assignment**, `==` is **comparison**.

---

## Boolean Operators
Used to combine conditions.

### `and`
Both conditions must be true:
```python
True and True   # True
True and False  # False
```

### `or`
At least one condition must be true:
```python
True or False   # True
False or False  # False
```

### `not`
Reverses a boolean:
```python
not True   # False
not False  # True
```

---

## if Statements
Run code **only if** a condition is true.

```python
if condition:
    # code runs if condition is True
```

Example:
```python
age = 20

if age >= 18:
    print("You are an adult")
```

---

## if / else Statements
Choose between two paths.

```python
if condition:
    # runs if True
else:
    # runs if False
```

Example:
```python
if age < 18:
    print("Minor")
else:
    print("Adult")
```

---

## if / elif / else
Used when there are **multiple conditions**.

```python
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition2 is True
else:
    # runs if all above are False
```

Example:
```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

---

## while Loops
Repeat code **as long as a condition is true**.

```python
while condition:
    # repeats
```

Example:
```python
count = 0

while count < 5:
    print(count)
    count += 1
```

⚠️ Infinite loop if condition never becomes False.

---

## break Statements
Exit a loop immediately.

```python
while True:
    print("Enter your name")
    name = input()
    if name == "quit":
        break
```

---

## continue Statements
Skip the rest of the loop and start the next iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output:
```
0
1
3
4
```

---

## for Loops
Repeat code a **specific number of times**.

```python
for i in range(5):
    print(i)
```

### range() Behavior
- `range(5)` → 0 to 4
- `range(1, 5)` → 1 to 4
- `range(1, 10, 2)` → odd numbers

---

## import Statements
Import modules to use extra functionality.

```python
import random
```

Example:
```python
import random
print(random.randint(1, 10))
```

---

## Example: printRandom.py

```python
import random

for i in range(5):
    print(random.randint(1, 10))
```

What this does:
- Imports `random`
- Loops 5 times
- Prints a random number each time

---

## Common Beginner Mistakes

❌ Forgetting to save the file before running
❌ Using `=` instead of `==`
❌ Infinite `while` loops
❌ Incorrect indentation
❌ Running the wrong file

---

## Debugging Tip (Very Important)
Use **temporary print statements** to see program flow:

```python
print("Start")
# code
print("End")
```

This tells you **what runs and what doesn’t**.

---

## Key Takeaways
- Booleans control decisions
- `if` statements branch logic
- Loops repeat work
- `break` and `continue` control loops
- Flow control is the foundation of automation

---

## What Comes Next (Chapter 3)
- Functions
- Reusable code
- Cleaner programs
- Less copy/paste

---

✅ You now know how to make Python **think and repeat**.

