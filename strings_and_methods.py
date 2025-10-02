import string

# -------------------------
# Basic literal, indexing, slicing
# -------------------------
s = "Hello, World!"  # string literal
print("Whole string:", s)
print("Index 0:", s[0])  # 'H'
print("Last char:", s[-1])  # '!'
print("Slice [7:12]:", s[7:12])  # 'World'

# -------------------------
# Escape sequences and raw / multiline strings
# -------------------------
print("Line1\\nLine2 -> demonstrates newline:")
print("Line1\nLine2")  # newline
print(r"C:\\Users\\you\\file.txt  <-- raw string shows backslashes as-is")
multiline = """This is a
multi-line string.
It preserves the newlines."""
print("Multiline preview:\n", multiline)

# -------------------------
# Common useful methods and their small semantics
# -------------------------
text = input("\nType a short sentence (try punctuation): ").strip()
print("Original:", repr(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())
print("Swap case:", text.swapcase())
print("Starts with 'The'?:", text.startswith("The"))
print("Ends with '.'?:", text.endswith("."))
print("Count of letter 'a':", text.count("a"))
print("Split into words:", text.split())  # default split on whitespace
print("Split (maxsplit=2):", text.split(maxsplit=2))
print("Partition on first space:", text.partition(" "))

# strip variants
raw = "   surrounded by spaces   \n"
print("strip():", repr(raw.strip()))
print("lstrip():", repr(raw.lstrip()))
print("rstrip():", repr(raw.rstrip()))

# -------------------------
# Join: build a string from list
# -------------------------
words = text.split()
joined = " | ".join(words)
print("Joined with ' | ':", joined)

# -------------------------
# Validation helpers (very useful for user input)
# -------------------------
token = input("\nEnter a short token (letters or digits): ")
print(
    "isalpha():",
    token.isalpha(),
    "  isdigit():",
    token.isdigit(),
    "  isalnum():",
    token.isalnum(),
)


# -------------------------
# Remove punctuation (simple normalization)
# -------------------------
def remove_punctuation(s):
    # Using str.translate is efficient and good to teach
    tbl = str.maketrans("", "", string.punctuation)
    return s.translate(tbl)


clean = remove_punctuation(text)
print("Without punctuation:", clean)


# 1) Palindrome checker (ignore punctuation / case / spaces)
def is_palindrome(s):
    s_clean = remove_punctuation(s).replace(" ", "").lower()
    return s_clean == s_clean[::-1]


p = input("\nTry a palindrome (or press Enter to skip): ").strip()
if p:
    print("Palindrome?", is_palindrome(p))

# 2) Extract initials from a full name
name = input("Enter your full name (first middle last): ").strip()
initials = "".join([part[0].upper() + "." for part in name.split() if part])
print("Initials:", initials if initials else "(no name provided)")

# 3) Word and character counts
sentence = input("Enter a sentence to count words/chars: ").strip()
words = sentence.split()
print("Word count:", len(words))
print("Character count (excluding spaces):", len(sentence.replace(" ", "")))

# 4) Leet-ify (small extension of replace chain)
orig = input("Enter a word to leet-ify (a->4,e->3,o->0,i->1): ").strip()
leet = orig.replace("a", "4").replace("e", "3").replace("o", "0").replace("i", "1")
print("Leet:", leet)
