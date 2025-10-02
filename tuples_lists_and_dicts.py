from copy import deepcopy
from collections import Counter

# -------------------------
# Tuples (immutable)
# -------------------------
coords = (10, 20)  # simple tuple
print("Tuple coords:", coords)
# coords[0] = 5  # would raise TypeError - tuples are immutable

# Tuple unpacking
x, y = coords
print("Unpacked x, y:", x, y)

# Single-item tuple needs a trailing comma
one = (42,)
print("Single-item tuple:", one, type(one))

# -------------------------
# Lists (mutable) - common operations
# -------------------------
fruits = ["apple", "banana"]
print("\nStart fruits:", fruits)

# add & insert
fruits.append("cherry")  # add to end
fruits.insert(1, "orange")  # insert at index 1
print("After append/insert:", fruits)

# extend vs append
more = ["kiwi", "pear"]
fruits.extend(more)  # add elements of iterable
print("After extend:", fruits)

# modify, remove, pop
fruits[1] = "blueberry"  # replace item
print("After replace:", fruits)
fruits.remove("kiwi")  # remove first occurrence
popped = fruits.pop()  # removes last element and returns it
print("After remove/pop:", fruits, "popped:", popped)

# clear the list
tmp = fruits.copy()
tmp.clear()
print("Cleared tmp list:", tmp)

# slicing and negative indices
L = [0, 1, 2, 3, 4, 5]
print("Slice L[2:5]:", L[2:5])
print("Last two items:", L[-2:])
print("Reversed (slice):", L[::-1])

# -------------------------
# Copying lists: shallow vs deep
# -------------------------
a = [[1], [2]]
shallow = list(a)  # or a.copy()
deep = deepcopy(a)
a[0].append(99)
print("\nAfter mutating a:")
print("original:", a)
print("shallow copy (shares nested lists):", shallow)
print("deep copy (independent):", deep)

# -------------------------
# enumerate, range, zip (indexed loops and parallel iteration)
# -------------------------
names = ["Ann", "Ben", "Carl"]
for idx, name in enumerate(names, start=1):
    print(f"{idx}. {name}")

ages = [30, 25, 40]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# -------------------------
# List comprehensions (concise lists)
# -------------------------
squares = [x * x for x in range(6)]
evens = [x for x in range(20) if x % 2 == 0]
print("\nSquares:", squares)
print("Evens:", evens)

# Flatten a list of lists (list comprehension)
matrix = [[1, 2], [3, 4], [5]]
flat = [item for row in matrix for item in row]
print("Flattened matrix:", flat)

# -------------------------
# Sets (unique items), useful for membership & dedup
# -------------------------
items = [1, 2, 2, 3, 4, 4]
unique = set(items)
print("\nItems:", items, "Unique set:", unique)
print("Is 2 in unique?", 2 in unique)

# -------------------------
# Dictionaries: basics and iteration
# -------------------------
person = {"name": "Sam", "age": 30}
print("\nPerson name:", person["name"])
person["city"] = "Brussels"
print("Safe access job (with default):", person.get("job", "No job listed"))

# Iterate keys, values, items
print("Dict keys:", list(person.keys()))
print("Dict values:", list(person.values()))
print("Dict items:")
for k, v in person.items():
    print(" ", k, "->", v)

# Sort a dictionary by key / value (returns list of tuples)
scores = {"Alice": 90, "Bob": 75, "Cathy": 88}
print("\nScores sorted by name (key):", sorted(scores.items()))
print(
    "Scores sorted by score (value):",
    sorted(scores.items(), key=lambda kv: kv[1], reverse=True),
)

# -------------------------
# Counting words (using Counter) - improved from manual tally
# -------------------------
sentence = input("\nEnter a sentence to count words: ").lower()
words = [w.strip(".,!?;:()[]\"'") for w in sentence.split()]  # simple token cleanup
counts = Counter(words)
print("Word counts (Counter):", counts)
most_common = counts.most_common(3)
print("Top 3 words:", most_common)


# -------------------------
# Small helper functions / challenges
# -------------------------
def flatten(list_of_lists):
    """Return a flattened list from a list of lists."""
    return [item for row in list_of_lists for item in row]


def unique_preserve_order(seq):
    """Return list of unique items preserving first-seen order."""
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


# Try flatten
nested = [[1, 2], [3, 4], [5, 6]]
print("\nFlatten nested:", flatten(nested))
print("Unique preserve order from [2,1,2,3,1]:", unique_preserve_order([2, 1, 2, 3, 1]))

# Challenge: top-k words from text (use counts above)
k = input("\nEnter k to show top-k words (or press Enter to skip): ").strip()
if k.isdigit():
    k = int(k)
    print(f"Top {k} words:", counts.most_common(k))

# Challenge: flatten & dedupe a list of lists then sort
lst_of_lsts = [[3, 1], [2, 3], [4]]
flat = flatten(lst_of_lsts)
print("Flattened:", flat)
print("Unique sorted:", sorted(set(flat)))


print("\nEnd of tuples, lists & dicts demo. Next: oop.py")
