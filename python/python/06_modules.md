# 06 – Modules and Imports

---

## What is a module?

- **Concept:** A module is a Python file (e.g. `mymodule.py`). You use code from it by importing: `import mymodule` or `from mymodule import something`.
- **മലയാളം:** ഒരു .py ഫയലാണ് മൊഡ്യൂൾ; മറ്റ് ഫയലിൽ അത് ഉപയോഗിക്കാൻ import ചെയ്യും.

---

## import module

- **Concept:** `import os` loads the whole module; use its contents as `os.path`, `os.getenv`, etc.
- **മലയാളം:** മൊഡ്യൂൾ മുഴുവനും ലോഡ് ചെയ്യും; മൊഡ്യൂൾ പേര് ഡോട്ട് ചേർത്ത് ഉപയോഗിക്കും.

```python
import os
print(os.getcwd())      # current directory
print(os.environ.get("HOME"))
```

---

## from module import name

- **Concept:** `from os import path` brings only `path` into your file; use as `path.join(...)` without `os.` prefix.
- **മലയാളം:** മൊഡ്യൂളിൽ നിന്ന് ഒരു പേര് മാത്രം എടുക്കും; ഉപയോഗിക്കുമ്പോൾ മൊഡ്യൂൾ പേര് വേണ്ട.

```python
from os import path
path.join("a", "b")   # "a/b" or "a\b"
```

---

## pip – install packages

- **Concept:** `pip install package_name` installs a third-party package. Use `pip3` on Linux if you use Python 3.
- **മലയാളം:** പുറത്ത് നിന്നുള്ള പാക്കേജ് ഇൻസ്റ്റാൾ ചെയ്യാൻ pip ഉപയോഗിക്കും.

```bash
pip3 install requests
pip3 install boto3
```

---

## Standard library (useful for DevOps)

- **Concept:** Python comes with built-in modules: `os`, `sys`, `subprocess`, `json`, `re`, `argparse`, `pathlib`, etc. No pip needed.
- **മലയാളം:** ഇവ പൈത്തണിനൊപ്പം വരും; ഡെവോപ്സ് സ്ക്രിപ്റ്റുകൾക്ക് os, subprocess, json, re എന്നിവ പലപ്പോഴും ഉപയോഗിക്കും.

```python
import os
import sys
import json
import subprocess
import re
```

---

## __name__ == "__main__"

- **Concept:** When you run a file directly, `__name__` is `"__main__"`. So `if __name__ == "__main__":` runs that block only when the file is executed, not when imported.
- **മലയാളം:** ഫയൽ നേരിട്ട് റൺ ചെയ്യുമ്പോൾ മാത്രം ആ ബ്ലോക്ക് എക്സിക്യൂട്ട് ചെയ്യാൻ ഉപയോഗിക്കും; import ചെയ്താൽ റൺ ആവില്ല.

```python
def main():
    print("Script running")

if __name__ == "__main__":
    main()
```

---

**Next:** **07_oop.md** – classes, objects, methods.
