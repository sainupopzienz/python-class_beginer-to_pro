# 03 – Functions

---

## Defining a function

- **Concept:** A function is a reusable block of code. Define with `def name():` and indent the body. Call with `name()`.
- **മലയാളം:** ഒരേ കോഡ് പലതവണ ഉപയോഗിക്കാൻ ഫങ്ഷൻ എഴുതും; `def name():` കൊണ്ട് നിർവചിക്കുക, `name()` കൊണ്ട് വിളിക്കുക.

```python
def greet():
    print("Hello")

greet()   # Hello
```

---

## Parameters (arguments)

- **Concept:** Parameters are variables you pass into the function. Put them inside parentheses in `def`.
- **മലയാളം:** ഫങ്ഷനിലേക്ക് കൊടുക്കുന്ന മൂല്യങ്ങൾ; ഡെഫ് ഇൻ പരന്റീസിസിൽ എഴുതും.

```python
def greet(name):
    print("Hello", name)

greet("Sainudeen")   # Hello Sainudeen
```

---

## Multiple parameters

- **Concept:** Separate parameters with commas. Call by passing same number of values in order.
- **മലയാളം:** പാരാമീറ്ററുകൾ കോമ കൊണ്ട് വേർതിരിക്കും; വിളിക്കുമ്പോൾ ഓർഡറിൽ മൂല്യങ്ങൾ കൊടുക്കും.

```python
def add(a, b):
    print(a + b)

add(3, 5)   # 8
```

---

## return

- **Concept:** `return value` sends a value back to the caller and ends the function. Without return, function returns `None`.
- **മലയാളം:** ഫങ്ഷനിൽ നിന്ന് ഒരു മൂല്യം തിരികെ കൊടുക്കാൻ `return` ഉപയോഗിക്കും; return ഇല്ലെങ്കിൽ None കിട്ടും.

```python
def add(a, b):
    return a + b

result = add(3, 5)   # result is 8
```

---

## Default arguments

- **Concept:** You can give a parameter a default value; if the caller doesn't pass it, the default is used.
- **മലയാളം:** പാരാമീറ്ററിന് ഒരു ഡിഫോൾട്ട് വില നൽകാം; വിളിക്കുമ്പോൾ കൊടുക്കാത്താൽ അത് ഉപയോഗിക്കും.

```python
def greet(name, msg="Hello"):
    print(msg, name)

greet("Ali")           # Hello Ali
greet("Ali", "Hi")     # Hi Ali
```

---

## Keyword arguments

- **Concept:** When calling, you can pass by name: `func(a=1, b=2)`. Order doesn't matter then.
- **മലയാളം:** വിളിക്കുമ്പോൾ പേര് കൊണ്ട് കൊടുക്കാം; ഓർഡർ മാറ്റാം.

```python
def info(name, age):
    print(name, age)

info(age=25, name="Sainudeen")
```

---

## *args (variable positional arguments)

- **Concept:** `*args` collects extra positional arguments into a tuple. Useful when you don't know how many will be passed.
- **മലയാളം:** അധിക പോസിഷണൽ ആർഗ്യുമെന്റുകൾ ഒരു ടപ്പിളായി കൈക്കൊള്ളും.

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))   # 6
```

---

## **kwargs (variable keyword arguments)

- **Concept:** `**kwargs` collects extra keyword arguments into a dictionary (key=value pairs).
- **മലയാളം:** അധിക കീ-വാല്യൂ ആർഗ്യുമെന്റുകൾ ഒരു ഡിക്ഷണറിയായി കൈക്കൊള്ളും.

```python
def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

show(name="Dev", role="DevOps")
```

---

**Next:** **04_data_structures.md** – list, dict, tuple, set.
