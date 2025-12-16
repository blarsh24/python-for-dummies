# Chapter 4 — Lists

**Disclaimer:** Although these notes were AI-generated, the code in the exercises folder was completed by me. This is solely to create a comprehensive, completed folder for each chapter of *Automate the Boring Stuff with Python*.

These notes cover **Chapter 4 of *Automate the Boring Stuff with Python***. This chapter introduces **lists**, one of the most important data structures in Python, used to store and work with multiple values.

---

## What Is a List?

A list is a **collection of values** stored in a single variable.

```python
spam = ["cat", "dog", "bat"]
```

* Lists are **ordered**
* Lists are **mutable** (can be changed)
* Lists use **zero-based indexing**

---

## Accessing List Items (Indexing)

```python
spam = ["cat", "dog", "bat"]
print(spam[0])  # cat
print(spam[1])  # dog
print(spam[2])  # bat
```

⚠️ Indexing starts at `0`, not `1`.

---

## Negative Indexes

Access items from the end of the list.

```python
spam = ["cat", "dog", "bat"]
print(spam[-1])  # bat
print(spam[-2])  # dog
```

---

## List Slices

Slices get **multiple items** from a list.

```python
spam = ["cat", "dog", "bat", "rat"]
print(spam[1:3])  # ['dog', 'bat']
print(spam[:2])   # ['cat', 'dog']
print(spam[1:])   # ['dog', 'bat', 'rat']
```

* End index is **exclusive**
* Omitting start or end uses defaults

---

## Changing List Values

Lists are mutable.

```python
spam = ["cat", "dog", "bat"]
spam[1] = "elephant"
print(spam)
```

---

## List Concatenation and Replication

```python
[1, 2] + [3, 4]    # [1, 2, 3, 4]
["Hi"] * 3        # ['Hi', 'Hi', 'Hi']
```

---

## Deleting Values from Lists

### Using `del`

```python
spam = ["cat", "dog", "bat"]
del spam[1]
print(spam)  # ['cat', 'bat']
```

---

## List Length with `len()`

```python
spam = ["cat", "dog", "bat"]
len(spam)  # 3
```

---

## Looping Through Lists

### Using `for`

```python
for animal in ["cat", "dog", "bat"]:
    print(animal)
```

### Using `range()` with indexes

```python
spam = ["cat", "dog", "bat"]
for i in range(len(spam)):
    print(i, spam[i])
```

---

## The `in` and `not in` Operators

Check if a value exists in a list.

```python
"dog" in ["cat", "dog", "bat"]      # True
"lion" not in ["cat", "dog", "bat"] # True
```

---

## Multiple Assignment

Assign multiple variables at once.

```python
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
```

⚠️ Number of variables must match list length.

---

## List Methods

### `append()`

Add item to end.

```python
spam.append("rat")
```

### `insert()`

Insert item at index.

```python
spam.insert(1, "chicken")
```

### `remove()`

Remove first matching value.

```python
spam.remove("cat")
```

### `sort()`

Sort list.

```python
spam.sort()
spam.sort(reverse=True)
```

⚠️ Cannot sort lists with mixed data types.

---

## The `random` Module with Lists

```python
import random

pets = ['cat', 'dog', 'fish']
random.choice(pets)
random.shuffle(pets)
```

---

## Example: Magic 8-Ball (List-Based)

```python
import random

responses = [
    "Yes",
    "No",
    "Maybe",
    "Ask again later"
]

print(random.choice(responses))
```

---

## Common Beginner Mistakes

❌ IndexError from out-of-range indexes
❌ Forgetting lists start at index 0
❌ Modifying list while iterating incorrectly
❌ Mixing strings and numbers when sorting

---

## Debugging Tips

* Print list and indexes when confused
* Use `len(list)` to verify bounds
* Use small test lists

---

## Key Takeaways

* Lists store multiple values in order
* Indexing and slicing are core skills
* Lists are mutable
* Looping through lists is very common
* List methods simplify common operations

---

## What Comes Next (Chapter 5)

* Dictionaries
* Key-value pairs
* More complex data structures

---

✅ You now understand how to **store, access, and manipulate collections of data** using lists.
