import math
import random
from statistics import mean, median
from fractions import Fraction

# -------------------------
# Basic types: int, float, complex
# -------------------------
i = 5  # integer
f = 2.5  # float
c = 3 + 4j  # complex number
print("i:", i, type(i))
print("f:", f, type(f))
print("c:", c, type(c))
print("i + f =", i + f)  # int + float -> float
print("complex example:", c.real, c.imag)

# -------------------------
# Division: / (true), // (floor), divmod
# -------------------------
a, b = 7, 3
print(f"\nDivision examples with a={a}, b={b}:")
print("a / b (true division) =", a / b)  # 2.333...
print("a // b (floor division) =", a // b)  # 2
print("a % b (modulo) =", a % b)  # 1
print("divmod(a, b) -> (quotient, remainder) =", divmod(a, b))

# -------------------------
# Power, pow(), operator precedence, augmented assignment
# -------------------------
print("\nPower and precedence:")
print("2 ** 3 =", 2**3)  # 8
print("pow(2, 3) =", pow(2, 3))  # 8
x = 10
x += 5  # same as x = x + 5
print("x after x += 5:", x)

# -------------------------
# Floating point precision and rounding
# -------------------------
print("\nFloating point and rounding:")
print("0.1 + 0.2 ->", 0.1 + 0.2)  # shows small precision artifact
print("Round to 3 decimals:", round(0.1 + 0.2, 3))
# Use math.isclose to compare floats safely
print("Is 0.1+0.2 close to 0.3?", math.isclose(0.1 + 0.2, 0.3))

# -------------------------
# Useful math functions
# -------------------------
print("\nmath module examples:")
print("sqrt(16) =", math.sqrt(16))
print("ceil(3.2) =", math.ceil(3.2))
print("floor(3.7) =", math.floor(3.7))
print("factorial(5) =", math.factorial(5))

# -------------------------
# Statistics helpers
# -------------------------
nums = [1, 4, 7, 10]
print("\nNumbers:", nums)
print("mean:", mean(nums))
print("median:", median(nums))

# -------------------------
# Fractions for exact rational arithmetic
# -------------------------
f1 = Fraction(1, 3)
f2 = Fraction(1, 6)
print("\nFractions:")
print("f1 + f2 =", f1 + f2)  # exact rational result
print("float(f1 + f2) =", float(f1 + f2))

# -------------------------
# Random (simulate dice)
# -------------------------
print("\nDice simulation - roll two dice:")
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
print("Dice:", d1, d2, "Total:", d1 + d2)


# -------------------------
# Interactive: read numbers safely and operate on lists
# -------------------------
def read_numbers(prompt="Enter numbers separated by space: "):
    raw = input(prompt).strip()
    if not raw:
        return []
    parts = raw.split()
    out = []
    for p in parts:
        try:
            out.append(float(p))
        except ValueError:
            print("Skipping non-number:", p)
    return out


nums = read_numbers("\nEnter some numbers to summarize (e.g. 1 2 3.5): ")
if nums:
    print("Count:", len(nums))
    print("Sum:", sum(nums))
    print("Mean (statistics.mean):", mean(nums))
    print("Min, Max:", min(nums), max(nums))
    # list comprehension example - convert to ints:
    ints = [int(x) for x in nums]
    print("As ints (via list comprehension):", ints)


# -------------------------
# Small challenge 1: Simple calculator
# -------------------------
def simple_calculator():
    print(
        "\nSimple calculator: enter expression like '2 + 3' (operators + - * / ** // %)."
    )
    expr = input("Expression: ").strip()
    try:
        # Very small, controlled eval — for beginners only
        allowed_names = {"__builtins__": None}
        result = eval(expr, allowed_names, {})
        print("Result:", result)
    except Exception as e:
        print("Could not evaluate expression:", e)


simple_calculator()


# -------------------------
# Small challenge 2: Compound interest
# -------------------------
def compound_interest(principal, rate, years, times_per_year=1):
    # rate is annual rate as decimal (0.05 for 5%)
    return principal * (1 + rate / times_per_year) ** (times_per_year * years)


try:
    p = float(input("\nCompound interest demo\nPrincipal (e.g. 1000): "))
    r = float(input("Annual rate in % (e.g. 5): ")) / 100.0
    t = int(input("Years (e.g. 3): "))
    n = int(input("Times compounded per year (default 1): ") or 1)
    final = compound_interest(p, r, t, n)
    print(f"Final amount after {t} years: {final:.2f}")
except Exception as e:
    print("Skipping compound interest demo (bad input):", e)


# -------------------------
# Small challenge 3: Roll many dice (simulation)
# -------------------------
def simulate_dice_rolls(n_rolls=1000):
    totals = []
    for _ in range(n_rolls):
        totals.append(random.randint(1, 6) + random.randint(1, 6))
    # quick summary
    from collections import Counter

    counts = Counter(totals)
    print("\nDice roll simulation summary (first 10 totals counts):")
    for total in sorted(list(counts.keys()))[:10]:
        print(total, "->", counts[total])


try:
    n = int(
        input("\nSimulate how many dice throws? (enter number, blank -> skip): ") or 0
    )
    if n:
        simulate_dice_rolls(n)
except Exception as e:
    print("Skipping simulation:", e)


# -------------------------
# Small challenge 4: Primality check (simple)
# -------------------------
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True


try:
    q = input("\nCheck a number for primality (blank to skip): ").strip()
    if q:
        n = int(q)
        print(f"{n} is prime? {is_prime(n)}")
except Exception as e:
    print("Skipping prime check:", e)

# -------------------------
# Quick note: complex numbers (brief)
# -------------------------
print("\nComplex numbers quick note:")
z = complex(2, -3)
print("z:", z, "abs(z):", abs(z), "conjugate:", z.conjugate())

# End
print("\nEnd of numbers & math demo. Next: functions_and_loops.py")
