# 05 – Strings and Files

---

## String methods (common)

- **Concept:** Strings have methods like `.upper()`, `.lower()`, `.strip()` (remove side spaces), `.split()` (split into list), `.join()` (join list to string).
- **മലയാളം:** ടെക്സ്റ്റ് മാറ്റാൻ ഈ മെത്തോഡുകൾ; strip = വശത്തെ സ്പേസ് നീക്കം, split = ഭാഗങ്ങളാക്കൽ, join = ഒന്നിപ്പിക്കൽ.

```python
s = "  Hello World  "
s.strip()           # "Hello World"
s.upper()           # "  HELLO WORLD  "
"a,b,c".split(",")  # ["a", "b", "c"]
" ".join(["a","b"]) # "a b"
```

---

## String formatting – f-string (recommended)

- **Concept:** Put variables inside `f"text {var}"` to embed their values in the string.
- **മലയാളം:** സ്ട്രിംഗിനുള്ളിൽ വേരിയബിളുകൾ കാണിക്കാൻ f-string ഉപയോഗിക്കുക.

```python
name = "DevOps"
print(f"Hello {name}")       # Hello DevOps
print(f"2+2 = {2+2}")        # 2+2 = 4
```

---

## Reading a file

- **Concept:** Open file with `open(path, "r")`, read with `.read()` or `.readlines()`, then close with `.close()`. Better: use `with` so it closes automatically.
- **മലയാളം:** ഫയൽ തുറന്ന് വായിക്കും; `with` ഉപയോഗിച്ചാൽ തുറന്ന ഫയൽ ഓട്ടോമാറ്റിക്കായി അടയ്ക്കും.

```python
with open("config.txt", "r") as f:
    content = f.read()       # entire file as string
# or
with open("config.txt", "r") as f:
    lines = f.readlines()    # list of lines
```

---

## Writing to a file

- **Concept:** Open with `"w"` to overwrite or `"a"` to append. Use `.write()` to write text. `with` closes the file.
- **മലയാളം:** `"w"` = മുഴുവൻ എഴുതി മാറ്റും, `"a"` = അവസാനത്തിൽ ചേർക്കും; write() കൊണ്ട് എഴുതും.

```python
with open("out.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
```

---

## File modes (short)

- **Concept:** `"r"` read, `"w"` write (overwrite), `"a"` append, `"r+"` read and write. Add `"b"` for binary (e.g. `"rb"`).
- **മലയാളം:** r=വായന, w=എഴുത്ത്(മാറ്റൽ), a=ചേർക്കൽ; b ചേർത്താൽ ബൈനറി.

---

## Paths and os.path

- **Concept:** `os.path.join("dir", "file.txt")` builds path correctly for your OS. `os.path.exists(path)` checks if file/folder exists.
- **മലയാളം:** ഓഎസിനനുസരിച്ച് path ശരിയായി ഉണ്ടാക്കാൻ join; ഫയൽ ഉണ്ടോ എന്ന് exists() കൊണ്ട് പരിശോധിക്കാം.

```python
import os
path = os.path.join("/etc", "nginx", "nginx.conf")
if os.path.exists(path):
    print("File exists")
```

---

**Next:** **06_modules.md** – import, pip, standard library.
