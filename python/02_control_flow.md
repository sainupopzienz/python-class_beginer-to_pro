# 02 – Control Flow (if, else, loops)

---

## if statement

- **Concept:** Run a block of code only when a condition is True. Use colon `:` and indent the block (same spaces).
- **മലയാളം:** നിബന്ധന സത്യമാകുമ്പോൾ മാത്രം ആ ബ്ലോക്ക് റൺ ചെയ്യും. `:` ഉം ഇൻഡെന്റും ശരിയായി ഇടുക.

```python
age = 20
if age >= 18:
    print("Adult")
```

---

## if – else

- **Concept:** If condition is True run first block; otherwise run the block under `else`.
- **മലയാളം:** നിബന്ധന സത്യമെങ്കിൽ മുകളിലത്തെ ബ്ലോക്ക്, അല്ലെങ്കിൽ `else` കീഴിലത്തെ ബ്ലോക്ക്.

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## if – elif – else

- **Concept:** `elif` = "else if". Check many conditions in order; first True one runs, then stop.
- **മലയാളം:** ഒന്നിലധികം നിബന്ധനകൾ ഓർഡറിൽ പരിശോധിക്കും; ആദ്യം സത്യമാകുന്നത് റൺ ചെയ്യും.

```python
score = 75
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")
```

---

## Indentation (spaces matter)

- **Concept:** Python uses indentation (usually 4 spaces) to show which lines belong to which block. No curly braces.
- **മലയാളം:** ബ്ലോക്ക് നിർവചിക്കാൻ സ്പേസുകൾ ഉപയോഗിക്കും; ഒരേ ബ്ലോക്കിൽ ഒരേ ഇൻഡെന്റ് വേണം.

---

## for loop

- **Concept:** Repeat a block for each item in a sequence (e.g. list, string, range). Use `for item in sequence:`.
- **മലയാളം:** സീക്വൻസിലെ ഓരോ ഇനത്തിനും ബ്ലോക്ക് ആവർത്തിക്കും.

```python
for i in [1, 2, 3]:
    print(i)   # 1, 2, 3

for char in "Hi":
    print(char)  # H, i
```

---

## range()

- **Concept:** `range(n)` gives 0 to n-1; `range(start, end)` gives start to end-1; `range(start, end, step)` uses step.
- **മലയാളം:** നമ്പറുകളുടെ സീക്വൻസ് നൽകും; ലൂപ്പിൽ ഉപയോഗിക്കാൻ സൗകര്യം.

```python
for i in range(5):      # 0, 1, 2, 3, 4
for i in range(2, 6):   # 2, 3, 4, 5
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
```

---

## while loop

- **Concept:** Keep running the block while the condition is True; stop when it becomes False.
- **മലയാളം:** നിബന്ധന സത്യമായിരിക്കുന്നിടത്തോളം ബ്ലോക്ക് ആവർത്തിക്കും.

```python
count = 0
while count < 3:
    print(count)
    count += 1   # same as count = count + 1
```

---

## break

- **Concept:** `break` exits the loop immediately (for or while).
- **മലയാളം:** ലൂപ്പിൽ നിന്ന് ഉടൻ പുറത്തുകടക്കാൻ `break` ഉപയോഗിക്കുക.

```python
for i in range(10):
    if i == 5:
        break
    print(i)   # 0,1,2,3,4
```

---

## continue

- **Concept:** `continue` skips the rest of the current iteration and goes to the next one.
- **മലയാളം:** ഇപ്പോഴത്തെ റൌണ്ട് ബാക്കി ഒഴിവാക്കി അടുത്ത റൌണ്ടിലേക്ക് പോകും.

```python
for i in range(4):
    if i == 2:
        continue
    print(i)   # 0, 1, 3
```

---

**Next:** **03_functions.md** – functions, arguments, return.
