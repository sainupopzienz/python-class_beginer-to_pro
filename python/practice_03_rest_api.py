# Practice 3: REST API and HTTP methods
# Run: pip3 install requests   (if not installed)
# Then: python3 practice_03_rest_api.py

import requests

# We use a free public API that allows GET: https://jsonplaceholder.typicode.com
BASE = "https://jsonplaceholder.typicode.com"

# --- GET: read data (no change on server) ---
print("=== GET example ===")
r = requests.get(f"{BASE}/posts/1")
print("Status:", r.status_code)   # 200 = OK
print("Response:", r.json())

# --- GET with query params ---
print("\n=== GET with params ===")
r = requests.get(f"{BASE}/posts", params={"userId": 1, "_limit": 2})
print("URL used:", r.url)
print("Count:", len(r.json()))

# --- POST: create (fake on this API – no real create) ---
print("\n=== POST example ===")
payload = {"title": "My post", "body": "Hello DevOps", "userId": 1}
r = requests.post(f"{BASE}/posts", json=payload)
print("Status:", r.status_code)   # 201 = Created (on real APIs)
print("Response:", r.json())

# --- PATCH: update some fields ---
print("\n=== PATCH example ===")
payload = {"title": "Updated title"}
r = requests.patch(f"{BASE}/posts/1", json=payload)
print("Status:", r.status_code)
print("Response:", r.json())

# --- DELETE ---
print("\n=== DELETE example ===")
r = requests.delete(f"{BASE}/posts/1")
print("Status:", r.status_code)   # 200 = OK

print("\nDone. Check 10_rest_api_and_http.md for HTTP methods summary.")
