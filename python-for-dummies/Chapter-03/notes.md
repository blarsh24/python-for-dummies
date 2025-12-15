# Chapter 3 — Functions

**Disclaimer:** Although these notes were AI-generated, the code in the exercises folder was completed by me. This is solely to create a comprehensive, completed folder for each chapter of *Automate the Boring Stuff with Python*.

These notes cover **Chapter 3 of *Automate the Boring Stuff with Python***. This chapter introduces **functions**, which let you **reuse code** and make programs cleaner and easier to manage.

---

## What Is a Function?

A function is a **named block of code** that performs a specific task and can be **called multiple times**.

```python
def hello():
    print("Hello!")

hello()  # call the function
```

### Key Points

* `def` defines the function
* The code inside must be indented
* Call the function by its name followed by `()`

---

## Function Arguments

Functions can accept **input values** (arguments). These are used inside the function.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Arsh")
```

* `name` is the parameter
* `"Arsh"` is the argument

---

## Return Values

Functions can **return a value** using `return`.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
```

* `return` sends the value back to the caller
* Without `return`, function gives `None`

---

## The `None` Value

* `None` is a special value representing **nothing**.
* If a function does not `return` anything, Python returns `None` by default.

```python
def say_hi():
    print("Hi")

x = say_hi()  # prints Hi
print(x)      # prints None
```

---

## Keyword Arguments

You can pass arguments by name instead of position.

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(name="Buddy", animal="dog")
```

* Makes code clearer and avoids mistakes with argument order

---

## Default Values

You can provide default values for parameters.

```python
def describe_pet(animal, name="Unknown"):
    print(f"I have a {animal} named {name}.")

describe_pet("cat")  # uses default name
```

---

## Variable Scope

* **Global variables:** defined outside functions, accessible anywhere
* **Local variables:** defined inside functions, only accessible there

```python
global_var = 10

def func():
    local_var = 5
    print(global_var)

func()       # prints 10
print(local_var)  # Error: not defined
```

---

## The `return` vs `print` Debate

* Use `print` to **show output**
* Use `return` to **send output to another part of your code**

```python
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print(result)  # 12
```

---

## Docstrings

Document your functions with a **docstring** (triple quotes). Useful for clarity.

```python
def add(a, b):
    """Return the sum of a and b"""
    return a + b

help(add)  # shows the docstring
```

---

## Example: Birthday Greeting Function

```python
def birthday(name, age):
    print(f"Happy Birthday {name}! You are {age} years old.")

birthday("Arsh", 26)
```

* Demonstrates **arguments**, **function calls**, and **string formatting**

---

## Common Beginner Mistakes

❌ Forgetting parentheses when calling a function
❌ Mis-indenting the function body
❌ Using a variable before defining it
❌ Confusing return value with print output

---

## Debugging Tip

* Add print statements to check what’s happening inside the function.
* Use `return` to test outputs instead of relying on prints.

---

## Key Takeaways

* Functions reduce code repetition
* Parameters and return values make functions flexible
* Keyword arguments and default values improve clarity
* Scope matters: local vs global
* Docstrings help document code

---

## What Comes Next (Chapter 4)

* Lists
* Accessing elements
* Modifying and iterating over lists
* Building more complex programs

---

✅ You now know how to **define, call, and manage functions** in Python.
