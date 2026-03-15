# 01 – Python Basics (Variables, Types, Operators)

---

## Running Python

- **Concept:** You run code with `python3 script.py` or type `python3` for interactive shell.
- **മലയാളം:** കോഡ് റൺ ചെയ്യാൻ `python3 script.py` ഉപയോഗിക്കുക; നേരിട്ട് ടെസ്റ്റ് ചെയ്യാൻ `python3` എഴുതി Enter അടിക്കുക.

---

## Variables

- **Concept:** A variable is a name that holds a value. You assign with `=`. No need to declare type.
- **മലയാളം:** വേരിയബിൾ = ഒരു പേര്, അതിന് കീഴിൽ ഒരു വില (value) സൂക്ഷിക്കും. ടൈപ്പ് പറയേണ്ടതില്ല.

```python
name = "Sainudeen"
count = 10
```

---

## Data Types (Basic)

| Type    | Example        | Meaning |
|---------|----------------|--------|
| int     | `42`           | Integer number |
| float   | `3.14`         | Decimal number |
| str     | `"hello"`      | Text (string) |
| bool    | `True`, `False`| Yes/No |

- **മലയാളം:** int = പൂർണ്ണസംഖ്യ, float = ദശാംശം, str = ടെക്സ്റ്റ്, bool = സത്യം/അസത്യം.

---

## Strings

- **Concept:** Text inside quotes (single or double). Use `+` to join, `*` to repeat.
- **മലയാളം:** ഉദ്ധരണികൾക്കുള്ളിൽ എഴുതിയ ടെക്സ്റ്റ്; കൂട്ടാൻ `+`, ആവർത്തിക്കാൻ `*`.

```python
a = "Hello"
b = 'World'
print(a + " " + b)   # Hello World
print(a * 2)         # HelloHello
```

---

## Comments

- **Concept:** `#` makes the rest of the line a comment; Python ignores it.
- **മലയാളം:** `#` ഇട്ടാൽ അവസാനം വരെയുള്ളത് കമന്റ്; Python അത് എണ്ണില.

```python
# This is a comment
x = 5  # inline comment
```

---

## print()

- **Concept:** `print()` shows output on the screen. You can pass variables or text.
- **മലയാളം:** `print()` സ്ക്രീനിൽ ഔട്ട്പുട്ട് കാണിക്കും.

```python
print("Hello")
print("Count:", count)
```

---

## Arithmetic Operators

| Operator | Meaning   | Example   |
|----------|-----------|-----------|
| `+`      | Add       | `3 + 2` → 5 |
| `-`      | Subtract  | `5 - 2` → 3 |
| `*`      | Multiply  | `4 * 3` → 12 |
| `/`      | Divide    | `10 / 4` → 2.5 |
| `//`     | Floor div | `10 // 4` → 2 |
| `%`      | Remainder | `10 % 4` → 2 |
| `**`     | Power     | `2 ** 3` → 8 |

- **മലയാളം:** `//` = ഹരണഫലം പൂർണ്ണസംഖ്യ, `%` = ശിഷ്ടം, `**` = ഘാതം.

---

## Comparison Operators (True/False)

| Operator | Meaning        | Example      |
|----------|----------------|--------------|
| `==`     | Equal          | `5 == 5` → True |
| `!=`     | Not equal      | `5 != 3` → True |
| `>`      | Greater than   | `5 > 3` → True |
| `<`      | Less than      | `2 < 4` → True |
| `>=`     | Greater or equal | `5 >= 5` → True |
| `<=`     | Less or equal  | `3 <= 5` → True |

- **മലയാളം:** ഇവ എല്ലാം ഒരു ഉത്തരം നൽകും: True അല്ലെങ്കിൽ False.

---

## type()

- **Concept:** `type(x)` tells you the data type of `x` (int, str, float, etc.).
- **മലയാളം:** `x` എന്ത് ടൈപ്പാണ് എന്ന് പറയാൻ `type(x)` ഉപയോഗിക്കുക.

```python
print(type(42))    # <class 'int'>
print(type("hi"))  # <class 'str'>
```

---

## input()

- **Concept:** `input("prompt")` reads one line from the user; result is always a string.
- **മലയാളം:** യൂസർ ടൈപ്പ് ചെയ്യുന്ന ഒരു വരി വായിക്കും; എല്ലായ്പ്പോഴും string ആയി കിട്ടും.

```python
name = input("Enter your name: ")
# If you need a number: count = int(input("Enter number: "))
```

---

## int() and str() – Type Conversion

- **Concept:** `int("42")` converts string to integer; `str(42)` converts number to string.
- **മലയാളം:** സ്ട്രിംഗിനെ നമ്പറാക്കാൻ `int()`, നമ്പറിനെ ടെക്സ്റ്റാക്കാൻ `str()`.

```python
x = int("10")   # x is 10 (number)
y = str(10)     # y is "10" (text)
```

---

**Next:** Open **02_control_flow.md** for if/else and loops.
