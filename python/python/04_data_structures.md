# 04 – Data Structures (List, Dict, Tuple, Set)

---

## List – ordered, changeable

- **Concept:** A list holds multiple values in order inside `[]`. You can add, remove, change items. Index starts at 0.
- **മലയാളം:** ഓർഡറിൽ മൂല്യങ്ങൾ സൂക്ഷിക്കും; മാറ്റാം, കൂട്ടാം, നീക്കാം. ആദ്യ ഇനം index 0.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])      # apple
print(fruits[-1])     # cherry (last)
fruits.append("mango")
len(fruits)           # 4
```

---

## List slicing

- **Concept:** `list[start:end]` gives items from index start to end-1. Omit start = from start; omit end = to end.
- **മലയാളം:** ഒരു ഭാഗം മാത്രം എടുക്കാൻ സ്ലൈസ് ഉപയോഗിക്കും; start/end വിട്ടാൽ ആ ഭാഗം വരെയൊക്കെ.

```python
nums = [10, 20, 30, 40, 50]
nums[1:4]   # [20, 30, 40]
nums[:3]    # [10, 20, 30]
nums[2:]    # [30, 40, 50]
```

---

## List methods (common)

- **Concept:** `.append(x)` add at end; `.insert(i, x)` add at index i; `.remove(x)` remove first x; `.pop()` remove and return last.
- **മലയാളം:** ലിസ്റ്റിൽ ഇനം ചേർക്കാനും നീക്കാനും ഈ മെത്തോഡുകൾ ഉപയോഗിക്കും.

```python
a = [1, 2, 3]
a.append(4)      # [1,2,3,4]
a.insert(0, 0)   # [0,1,2,3,4]
a.remove(2)      # [0,1,3,4]
a.pop()          # returns 4, list becomes [0,1,3]
```

---

## Dictionary – key: value pairs

- **Concept:** A dict stores key-value pairs in `{}`. Access by key: `d[key]`. Keys are unique; values can be anything.
- **മലയാളം:** കീ-വാല്യൂ ജോഡികൾ സൂക്ഷിക്കും; കീ കൊണ്ട് വാല്യൂ എടുക്കും. കീ യൂണിക്യൂ ആയിരിക്കണം.

```python
person = {"name": "Sainudeen", "role": "DevOps", "age": 25}
print(person["name"])   # Sainudeen
person["city"] = "Kochi"
"role" in person        # True
```

---

## Dict methods (common)

- **Concept:** `.keys()` all keys; `.values()` all values; `.items()` (key, value) pairs; `.get(key, default)` safe access.
- **മലയാളം:** കീകൾ, വാല്യൂകൾ, ജോഡികൾ എടുക്കാൻ; കീ ഇല്ലെങ്കിൽ ഡിഫോൾട്ട് കിട്ടാൻ `.get()`.

```python
person.get("name")       # Sainudeen
person.get("x", "N/A")   # N/A (key not found)
for k, v in person.items():
    print(k, v)
```

---

## Tuple – ordered, immutable

- **Concept:** Like a list but you cannot change it after creation. Use `()`. Good for fixed data (e.g. coordinates).
- **മലയാളം:** ലിസ്റ്റ് പോലെയാണ്; സൃഷ്ടിച്ച ശേഷം മാറ്റാൻ പാടില്ല. `()` ഉപയോഗിക്കും.

```python
point = (10, 20)
print(point[0])   # 10
# point[0] = 5   # Error – cannot change
```

---

## Set – unique, unordered

- **Concept:** A set holds unique values only (no duplicates), in no fixed order. Use `{}` with values only, or `set()`.
- **മലയാളം:** ഡ്യുപ്ലിക്കേറ്റ് ഇല്ല; ഓർഡർ ഉറപ്പില്ല. യൂണിക്യൂ ഇനങ്ങൾ സൂക്ഷിക്കാൻ.

```python
tags = {"docker", "kubernetes", "docker"}   # {"docker", "kubernetes"}
tags.add("ansible")
"docker" in tags   # True
```

---

## Looping over structures

- **Concept:** `for item in list:` over items; `for key in dict:` over keys; `for k, v in dict.items():` over pairs.
- **മലയാളം:** ലിസ്റ്റിൽ ഇനം കൊണ്ട്, ഡിക്ഷണറിയിൽ കീ അല്ലെങ്കിൽ items() കൊണ്ട് ലൂപ്പ് ചെയ്യാം.

```python
for x in [1, 2, 3]:
    print(x)
for k, v in {"a": 1, "b": 2}.items():
    print(k, v)
```

---

**Next:** **05_strings_and_files.md** – string methods, file read/write.
