# 10 – REST API and HTTP Methods

---

## What is an API?

- **Concept:** API = Application Programming Interface. It is a way for two programs to talk to each other over the network (send and receive data).
- **മലയാളം:** API = രണ്ട് പ്രോഗ്രാമുകൾ തമ്മിൽ നെറ്റ്വർക്കിലൂടെ സംവദിക്കാൻ ഉള്ള മാർഗം; ഡാറ്റ അയച്ചും വാങ്ങിയും കൊള്ളാം.

---

## What is REST API?

- **Concept:** REST = Representational State Transfer. A REST API uses HTTP (same protocol as browsers) to get or send data. You call a URL and get back data (often JSON).
- **മലയാളം:** REST API = HTTP ഉപയോഗിച്ച് ഡാറ്റ കൊടുക്കാനും വാങ്ങാനും ഉള്ള ഒരു രീതി; URL വിളിച്ച് ഡാറ്റ (പലപ്പോഴും JSON) കിട്ടും.

---

## What is HTTP?

- **Concept:** HTTP = HyperText Transfer Protocol. It is the protocol used when you open a website or call an API. Every request has a method (GET, POST, etc.) and a URL.
- **മലയാളം:** HTTP = വെബ് പേജ് അല്ലെങ്കിൽ API വിളിക്കുമ്പോൾ ഉപയോഗിക്കുന്ന നിയമം; ഓരോ റിക്വെസ്റ്റിനും ഒരു method ഉം URL ഉം ഉണ്ട്.

---

## HTTP methods (short meaning)

| Method   | Meaning in simple words | When to use |
|----------|--------------------------|-------------|
| **GET**  | "Give me data"           | Read / fetch something (no change on server) |
| **POST** | "Create something new"   | Create a new resource (e.g. new user, new order) |
| **PUT**  | "Replace entire thing"   | Update by replacing the whole resource |
| **PATCH**| "Update only some fields"| Update only part of a resource |
| **DELETE**| "Remove it"             | Delete a resource |

- **മലയാളം:** GET = ഡാറ്റ വാങ്ങാൻ, POST = പുതിയത് സൃഷ്ടിക്കാൻ, PUT = മുഴുവൻ മാറ്റാൻ, PATCH = ചില ഫീൽഡുകൾ മാത്രം മാറ്റാൻ, DELETE = ഇല്ലാതാക്കാൻ.

---

## GET – read data (no change)

- **Concept:** GET is used to **read** or **fetch** data. It does not change anything on the server. Example: get list of users, get status of a service.
- **മലയാളം:** ഡാറ്റ വായിക്കാനോ വാങ്ങാനോ GET ഉപയോഗിക്കും; സർവറിൽ ഒന്നും മാറ്റില്ല.

```python
import requests
r = requests.get("https://api.example.com/users")
print(r.status_code)   # 200 = success
print(r.json())        # response body as Python dict/list
```

---

## POST – create something new

- **Concept:** POST is used to **create** a new resource. You send data in the request body (e.g. JSON). Example: create user, create order, trigger a job.
- **മലയാളം:** പുതിയ ഒന്ന് സൃഷ്ടിക്കാൻ POST; ബോഡിയിൽ ഡാറ്റ അയക്കും (ഉദാ. JSON).

```python
import requests
payload = {"name": "Sainudeen", "role": "DevOps"}
r = requests.post("https://api.example.com/users", json=payload)
print(r.status_code)   # 201 = created (often)
print(r.json())
```

---

## PUT – replace entire resource

- **Concept:** PUT is used to **replace** the whole resource at that URL. You send the full new data. Example: update entire user profile.
- **മലയാളം:** ആ URL-ലെ മുഴുവൻ റിസോഴ്സും മാറ്റി എഴുതാൻ PUT; പുതിയ മുഴുവൻ ഡാറ്റയും അയക്കും.

```python
payload = {"name": "Sainudeen", "role": "DevOps", "age": 26}
r = requests.put("https://api.example.com/users/1", json=payload)
```

---

## PATCH – update only some fields

- **Concept:** PATCH is used to **update only some fields**, not the whole resource. You send only what changed. Example: update only email or status.
- **മലയാളം:** ചില ഫീൽഡുകൾ മാത്രം മാറ്റാൻ PATCH; മാറിയ ഭാഗം മാത്രം അയക്കും.

```python
payload = {"role": "Senior DevOps"}
r = requests.patch("https://api.example.com/users/1", json=payload)
```

---

## DELETE – remove resource

- **Concept:** DELETE is used to **remove** the resource at that URL. No body needed usually. Example: delete user, delete a record.
- **മലയാളം:** ആ റിസോഴ്സ് ഇല്ലാതാക്കാൻ DELETE; ബോഡി സാധാരണയായി വേണ്ട.

```python
r = requests.delete("https://api.example.com/users/1")
print(r.status_code)   # 200 or 204 = success
```

---

## HTTP status codes (common)

| Code | Meaning |
|------|---------|
| 200 | OK – request succeeded (GET, PUT, PATCH) |
| 201 | Created – resource created (POST) |
| 204 | No Content – success, no body in response (often DELETE) |
| 400 | Bad Request – your request data is wrong |
| 401 | Unauthorized – need to login / provide token |
| 403 | Forbidden – not allowed |
| 404 | Not Found – URL or resource does not exist |
| 500 | Server Error – something broke on server |

- **മലയാളം:** 200 = സക്സസ്, 201 = സൃഷ്ടിച്ചു, 404 = കണ്ടില്ല, 401 = ലോഗിൻ/ടോക്കൺ വേണം, 500 = സർവർ പിശക്.

---

## URL and query parameters

- **Concept:** Base URL is like `https://api.example.com/users`. Query parameters come after `?`: `?page=1&limit=10`. Used often with GET to filter or paginate.
- **മലയാളം:** URL-ന് ശേഷം `?` ഇട്ട് key=value ചേർത്താൽ query parameter; GET-ൽ ഫിൽട്ടർ/പേജിനേഷൻക്ക് ഉപയോഗിക്കും.

```python
r = requests.get("https://api.example.com/users", params={"page": 1, "limit": 10})
# Actually calls: .../users?page=1&limit=10
```

---

## Request headers (common)

- **Concept:** Headers carry extra info: `Content-Type` (e.g. application/json), `Authorization` (token/Bearer for auth). You can set them in requests.
- **മലയാളം:** ഹെഡറുകൾ കൂടുതൽ വിവരം കൊണ്ടുപോകും; ഓഥൻറിക്കേഷൻ, ടൈപ്പ് എന്നിവ.

```python
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer your_token_here"
}
r = requests.get("https://api.example.com/me", headers=headers)
```

---

## Sending JSON in body (POST/PUT/PATCH)

- **Concept:** Use `json=payload` in requests; the library sets Content-Type and converts dict to JSON. Or use `data=json.dumps(payload)` and set header yourself.
- **മലയാളം:** `json=payload` ഉപയോഗിച്ചാൽ ഡിക്ഷണറി ഓട്ടോമാറ്റിക്കായി JSON ആയി അയക്കും; Content-Type യും സെറ്റ് ചെയ്യും.

```python
payload = {"name": "Dev", "env": "prod"}
r = requests.post(url, json=payload)
```

---

## Summary – one line each

| Topic | One line |
|-------|----------|
| API | Two programs talking over network. |
| REST API | API using HTTP and URLs; data often in JSON. |
| GET | Read data; no change on server. |
| POST | Create new resource; send data in body. |
| PUT | Replace whole resource. |
| PATCH | Update only some fields. |
| DELETE | Remove resource. |
| Status 200/201 | Success. 404 = not found, 401 = auth needed, 500 = server error. |

**മലയാളം:** API = പ്രോഗ്രാമുകൾ തമ്മിൽ സംവാദം. REST = HTTP + URL + JSON. GET വായന, POST സൃഷ്ടിക്കൽ, PUT മുഴുവൻ മാറ്റൽ, PATCH ഭാഗിക മാറ്റൽ, DELETE ഇല്ലാതാക്കൽ. 200/201 സക്സസ്; 404 കണ്ടില്ല, 401 ഓഥ് വേണം.

---

**Next:** Use **09_devops_scripts.md** for more on `requests` and **practice_03_rest_api.py** to try these methods.
