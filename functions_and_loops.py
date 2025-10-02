"""
functions_and_loops.py
Expanded interactive examples for functions, loops, and small patterns.
Run in a terminal (these use input()).
"""

from typing import List


# -------------------------
# Functions: docstring, return vs print, defaults, keyword args
# -------------------------
def greet(name: str, excited: bool = False) -> str:
    """Return a greeting string for `name`. Use `excited=True` to add an exclamation."""
    base = f"Hello, {name}"
    return base + "!" if excited else base


# Using the function
print(greet("Alice"))  # prints the returned string
print(greet("Bob", excited=True))  # positional arg
print(greet(name="Cara", excited=False))  # keyword args

# Important note:
# - Functions should return values (use `return`) so callers can reuse results.
# - Use `print()` only when you want immediate console output.


# -------------------------
# Type hints (optional help for learners)
# -------------------------
def add(a: float, b: float) -> float:
    """Return the sum of a and b (type hints are just hints)."""
    return a + b


print("Add example:", add(2, 3.5))

# -------------------------
# Lambdas, map, filter (short intro)
# -------------------------
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))  # same as [x*x for x in numbers]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Numbers:", numbers)
print("Squares (map+lambda):", squares)
print("Evens (filter+lambda):", evens)

# -------------------------
# List comprehensions and generator expressions
# -------------------------
doubles = [x * 2 for x in numbers if x > 2]  # comprehension with a condition
gen = (x * 2 for x in numbers)  # generator expression (lazy)
print("Doubles (list comp):", doubles)
print("Gen first value (next):", next(gen))

# -------------------------
# For loops with enumerate & zip
# -------------------------
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}. {fruit}")

names = ["Ann", "Ben", "Carl"]
ages = [28, 34, 22]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# -------------------------
# While loop example & safe loop input
# -------------------------
count = 3
while count > 0:
    print("Counting down:", count)
    count -= 1

# Safe repeated input: keep asking until user enters a valid int or blank to quit
while True:
    raw = input("\nEnter an integer (or press Enter to continue): ").strip()
    if raw == "":
        break
    try:
        val = int(raw)
        print("You entered:", val)
    except ValueError:
        print("That's not an integer — try again.")


# -------------------------
# Small reusable functions + list processing
# -------------------------
def f_to_c(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


# Interactive: convert a list of Fahrenheit temps
raw = input(
    "\nEnter temperatures in F separated by spaces (or leave blank to skip): "
).strip()
if raw:
    parts = raw.split()
    temps_c = []
    for p in parts:
        try:
            f = float(p)
            temps_c.append(f_to_c(f))
        except ValueError:
            print("Skipping non-number:", p)
    print("Celsius values:", [f"{c:.1f}" for c in temps_c])


# Challenge: compute the average of a numeric list
def average(nums: List[float]) -> float:
    """Return the average of nums (None-safe not included here)."""
    return sum(nums) / len(nums) if nums else 0.0


nums = [1.0, 2.5, 3.5]
print("Average of", nums, "is", average(nums))


# -------------------------
# Simple recursion (factorial)
# -------------------------
def factorial(n: int) -> int:
    """Simple recursive factorial. Explain base case to students."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print("Factorial 5:", factorial(5))
# Teaching note: recursion builds a call stack. For beginners, keep depth small.


# -------------------------
# Break/continue examples (short)
# -------------------------
print("\nLoop demo with break/continue:")
for i in range(1, 10):
    if i == 5:
        print("Skipping 5")
        continue
    if i == 8:
        print("Stopping at 8")
        break
    print("i =", i)

# -------------------------
# Error handling inside loops - robust processing
# -------------------------
raw = input("\nEnter numbers separated by spaces for safe processing: ").strip()
if raw:
    values = []
    for token in raw.split():
        try:
            values.append(float(token))
        except ValueError:
            # don't stop the whole program because of one bad token
            print("Warning: skipping non-number token:", token)
    print("Processed numeric values:", values)


print("\nEnd of functions & loops demo. Next: conditional logic and control flow.")
