import math


# -------------------------
# Safe integer input helper
# -------------------------
def read_int(prompt, default=None):
    raw = input(prompt).strip()
    if raw == "" and default is not None:
        return default
    try:
        return int(raw)
    except ValueError:
        print(
            "That's not a valid integer. Using default."
            if default is not None
            else "Invalid input."
        )
        return default


# -------------------------
# Comparisons and booleans
# -------------------------
x = read_int("Pick a number (or press Enter for 0): ", default=0)
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# boolean operators and chained comparisons
a = read_int("\nEnter a for 'a < b < c' demo (or blank -> 1): ", default=1)
b = read_int("Enter b (or blank -> 2): ", default=2)
c = read_int("Enter c (or blank -> 3): ", default=3)

print(f"Check chained comparison {a} < {b} < {c}:", a < b < c)
print("Logical examples:")
print("a < b and b < c ->", a < b and b < c)
print("a < b or b > c ->", a < b or b > c)
print("not (a == b) ->", not (a == b))

# truthiness (empty vs non-empty)
sample = input("\nType something (empty input shows falsy): ").strip()
if sample:
    print("You typed something, truthy:", sample)
else:
    print("You typed nothing (falsy)")

# ternary operator (short if/else expression)
msg = "positive" if x > 0 else ("zero" if x == 0 else "negative")
print("Your number is", msg)

# -------------------------
# Control flow in loops: continue, break, for-else and while-else
# -------------------------
print("\nLoop demo with continue/break/else:")
for i in range(1, 10):
    if i == 5:
        print("Skipping 5")
        continue
    if i == 8:
        print("Stopping at 8 (break)")
        break
    print("i =", i)
else:
    # runs only if loop completes without break
    print("Loop finished normally (no break)")

# while-else example: search for a value, else runs when not found
target = read_int(
    "\nEnter a small target number to find (1-5), blank to skip: ", default=None
)
if target is not None:
    found = False
    i = 1
    while i <= 5:
        if i == target:
            print("Found target:", i)
            found = True
            break
        i += 1
    else:
        print("Did not find the target in 1..5")


# -------------------------
# Factor finder (efficient up to sqrt(n))
# -------------------------
def factors(n):
    """Return sorted list of factors of n."""
    if n <= 0:
        return []
    small = []
    large = []
    k = 1
    while k * k <= n:
        if n % k == 0:
            small.append(k)
            if k != n // k:
                large.append(n // k)
        k += 1
    return sorted(small + large)


n = read_int(
    "\nEnter a positive integer to find its factors (or blank to skip): ", default=None
)
if n:
    print(f"Factors of {n}:", factors(n))


# -------------------------
# Prime test (simple, efficient)
# -------------------------
def is_prime(n):
    """Return True if n is probably prime (deterministic for n < 2^64 with this simple test)."""
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


q = read_int("\nCheck primality for a number (blank to skip): ", default=None)
if q is not None:
    print(f"{q} is prime? {is_prime(q)}")


# -------------------------
# Small extra algorithms: GCD (Euclid) and leap year
# -------------------------
def gcd(a, b):
    """Euclid's algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


a = read_int("\nEnter a for gcd(a, b) (blank to skip): ", default=None)
if a is not None:
    b = read_int("Enter b for gcd(a, b): ", default=0)
    print(f"gcd({a}, {b}) =", gcd(a, b))


def is_leap_year(year):
    """Return True for Gregorian leap years."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


year = read_int("\nEnter a year to test for leap year (blank to skip): ", default=None)
if year is not None:
    print(f"{year} is a leap year? {is_leap_year(year)}")


print("\nEnd of conditional logic & control flow demo.")
