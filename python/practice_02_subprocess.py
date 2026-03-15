# Practice 2: Run a shell command from Python (DevOps useful)
# ഷെൽ കമാൻഡ് പൈത്തണിൽ നിന്ന് റൺ ചെയ്യാൻ

import subprocess

# Try: ls -la (or dir on Windows)
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print("Return code:", result.returncode)
print("Output:")
print(result.stdout)
