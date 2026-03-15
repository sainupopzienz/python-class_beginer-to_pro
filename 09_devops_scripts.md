# 09 – Python for DevOps (Scripts, Commands, APIs)

---

## subprocess – run shell commands

- **Concept:** `subprocess.run(["cmd", "arg1"])` runs a command from Python and waits for it. You get return code and output.
- **മലയാളം:** പൈത്തണിൽ നിന്ന് ഷെൽ കമാൻഡ് റൺ ചെയ്യാൻ subprocess ഉപയോഗിക്കും; return code, output കിട്ടും.

```python
import subprocess
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.returncode)   # 0 = success
print(result.stdout)
```

---

## subprocess – capture_output and text

- **Concept:** `capture_output=True` captures stdout and stderr. `text=True` gives you strings instead of bytes.
- **മലയാളം:** കമാൻഡ് ഔട്ട്പുട്ട് കൈക്കൊള്ളാൻ capture_output; ടെക്സ്റ്റ് ആയി കിട്ടാൻ text=True.

```python
r = subprocess.run(["docker", "ps"], capture_output=True, text=True)
print(r.stdout)
```

---

## Environment variables

- **Concept:** `os.environ` is a dict of environment variables. Use `os.environ.get("VAR")` for safe access (returns None if missing). Use `os.getenv("VAR", "default")` for a default.
- **മലയാളം:** എൻവിറോൺമെന്റ് വേരിയബിളുകൾ os.environ-ൽ; get ഉപയോഗിച്ചാൽ ഇല്ലെങ്കിൽ None അല്ലെങ്കിൽ ഡിഫോൾട്ട്.

```python
import os
home = os.environ.get("HOME")
api_key = os.getenv("API_KEY", "")
```

---

## Command-line arguments – sys.argv

- **Concept:** `sys.argv` is a list: argv[0] is script name, argv[1], argv[2]... are arguments you pass. Simple but limited.
- **മലയാളം:** സ്ക്രിപ്റ്റ് വിളിക്കുമ്പോൾ കൊടുക്കുന്ന ആർഗ്യുമെന്റുകൾ sys.argv-ൽ; [0]=സ്ക്രിപ്റ്റ് പേര്, [1]=ആദ്യ ആർഗ്യുമെന്റ്.

```python
import sys
# python3 script.py arg1 arg2
print(sys.argv[0])   # script.py
print(sys.argv[1])   # arg1
```

---

## argparse – better CLI arguments

- **Concept:** `argparse` lets you define optional and required arguments, help text, and types. Standard way to build CLI tools.
- **മലയാളം:** ആർഗ്യുമെന്റുകൾക്ക് പേര്, ടൈപ്പ്, ഹെൽപ്പ് നൽകാൻ argparse ഉപയോഗിക്കും.

```python
import argparse
p = argparse.ArgumentParser()
p.add_argument("--host", default="localhost")
p.add_argument("--port", type=int, default=8080)
args = p.parse_args()
print(args.host, args.port)
# python3 script.py --host 0.0.0.0 --port 9000
```

---

## JSON – parse and dump

- **Concept:** `json.loads(string)` converts JSON string to Python dict/list. `json.dumps(dict)` converts Python object to JSON string. For files: `json.load(f)` and `json.dump(obj, f)`.
- **മലയാളം:** JSON സ്ട്രിംഗിനെ ഡിക്ഷണറിയാക്കാൻ loads; ഡിക്ഷണറിയെ JSON ആക്കാൻ dumps. ഫയലിന് load/dump.

```python
import json
data = json.loads('{"name": "dev"}')   # dict
s = json.dumps({"name": "dev"})       # '{"name": "dev"}'
with open("config.json") as f:
    config = json.load(f)
```

---

## requests – HTTP API calls (install with pip)

- **Concept:** `requests.get(url)` fetches a URL and returns a response. Use `.json()` to get response as dict, `.status_code` for HTTP status.
- **മലയാളം:** HTTP റിക്വെസ്റ്റ് അയക്കാൻ requests ഉപയോഗിക്കും; .json() കൊണ്ട് റിസ്പോൻസ് ഡിക്ഷണറിയാക്കാം.

```python
import requests
r = requests.get("https://api.example.com/status")
print(r.status_code)   # 200
print(r.json())
```

---

## Reading config files (YAML – optional)

- **Concept:** For YAML configs use `pip install pyyaml` then `yaml.safe_load(f)` to get a dict. Common in Kubernetes, Ansible, Docker Compose.
- **മലയാളം:** YAML ഫയലുകൾ വായിക്കാൻ PyYAML; safe_load കൊണ്ട് ഡിക്ഷണറി കിട്ടും. K8s, Ansible എന്നിവയിൽ പലപ്പോഴും.

```python
import yaml
with open("config.yaml") as f:
    config = yaml.safe_load(f)
```

---

## Regular expressions – re (short)

- **Concept:** `re.search(pattern, text)` finds first match; `re.findall(pattern, text)` finds all. Useful for parsing log lines or config.
- **മലയാളം:** ടെക്സ്റ്റിൽ പാറ്റേൺ തിരയാൻ re ഉപയോഗിക്കും; ലോഗ്/കോൺഫിഗ് പാർസ് ചെയ്യാൻ.

```python
import re
m = re.search(r"\d+", "Port 8080")   # 8080
ips = re.findall(r"\d+\.\d+\.\d+\.\d+", log_line)
```

---

## Summary for DevOps

- Use **subprocess** to run `docker`, `kubectl`, `aws`, shell scripts.
- Use **os.environ / getenv** for secrets and config (never hardcode).
- Use **argparse** for script options (--env, --region, etc.).
- Use **json** for API responses, config files, Terraform output.
- Use **requests** for health checks, webhooks, REST APIs.
- Use **try/except** so one failed step doesn’t crash the whole script.

**മലയാളം:** ഡെവോപ്സിൽ – കമാൻഡുകൾ subprocess, സീക്രട്ടുകൾ env-ൽ, ഓപ്ഷനുകൾ argparse, API/കോൺഫിഗ് json, HTTP requests, പിശകുകൾ try/except കൊണ്ട് ഹാൻഡിൽ ചെയ്യുക.

---

**You’ve completed the guide.** Practice by writing small scripts (e.g. list files, call an API, parse JSON). Revise from **01_basics.md** whenever needed.
