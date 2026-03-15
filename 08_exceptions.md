# 08 – Exceptions (Error Handling)

---

## What is an exception?

- **Concept:** When something goes wrong (e.g. file not found, divide by zero), Python raises an exception. If not caught, the program stops with an error message.
- **മലയാളം:** പിശക് സംഭവിക്കുമ്പോൾ Python ഒരു exception എറിയും; പിടിക്കാത്താൽ പ്രോഗ്രാം നിർത്തും.

---

## try and except

- **Concept:** Put risky code in `try:` block. If an exception occurs, the `except:` block runs. Rest of program can continue.
- **മലയാളം:** അപകടമുള്ള കോഡ് try-ൽ ഇടുക; പിശക് വന്നാൽ except ബ്ലോക്ക് റൺ ചെയ്യും.

```python
try:
    x = int("hello")   # raises ValueError
except ValueError:
    print("Invalid number")
```

---

## Catching specific exceptions

- **Concept:** You can write `except ValueError:`, `except FileNotFoundError:`, etc. Only that type of error is caught; others will still stop the program.
- **മലയാളം:** ഓരോ തരം പിശകിനും വെവ്വേറെ except എഴുതാം; അത് മാത്രം പിടിക്കും.

```python
try:
    f = open("missing.txt")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No permission")
```

---

## except Exception (broad)

- **Concept:** `except Exception:` catches almost all errors. Use when you want to catch "any error"; for logging or generic fallback.
- **മലയാളം:** ഏത് പിശകും പിടിക്കാൻ Exception ഉപയോഗിക്കാം; വളരെ പൊതുവായ ഹാൻഡ്ലിംഗിന്.

```python
try:
    risky_operation()
except Exception as e:
    print("Error:", e)
```

---

## else and finally

- **Concept:** `else:` block runs if no exception occurred. `finally:` block always runs (after try/except), useful for cleanup (e.g. closing file).
- **മലയാളം:** exception വന്നില്ലെങ്കിൽ else; എപ്പോഴും finally റൺ ചെയ്യും – ക്ലീനപ്പിന് ഉപയോഗിക്കാം.

```python
try:
    f = open("file.txt")
except FileNotFoundError:
    print("Not found")
else:
    print(f.read())
finally:
    f.close()   # always close
```

---

## raise – throw an exception

- **Concept:** You can raise an exception yourself with `raise ValueError("message")`. Use when your code detects an invalid state.
- **മലയാളം:** നിങ്ങൾ തന്നെ പിശക് എറിയാൻ raise ഉപയോഗിക്കും; അസാധുവായ സ്ഥിതി കണ്ടാൽ.

```python
def set_port(port):
    if port < 1 or port > 65535:
        raise ValueError("Port must be 1-65535")
    self.port = port
```

---

**Next:** **09_devops_scripts.md** – subprocess, env, JSON, APIs (DevOps-focused).
