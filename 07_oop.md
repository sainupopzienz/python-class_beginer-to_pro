# 07 – Object-Oriented Programming (OOP)

---

## Class and object

- **Concept:** A class is a blueprint; an object is one actual thing created from that blueprint. You define a class with `class Name:` and create objects with `Name()`.
- **മലയാളം:** ക്ലാസ് = ഡിസൈൻ; ഒബ്ജക്റ്റ് = അതിൽ നിന്നുള്ള ഒരു ഉദാഹരണം. ക്ലാസ് നിർവചിച്ച് ഒബ്ജക്റ്റ് സൃഷ്ടിക്കും.

```python
class Server:
    pass

s1 = Server()
s2 = Server()
```

---

## __init__ (constructor)

- **Concept:** `__init__(self, ...)` runs when you create an object. Use it to set initial attributes (e.g. name, port). `self` refers to the object itself.
- **മലയാളം:** ഒബ്ജക്റ്റ് സൃഷ്ടിക്കുമ്പോൾ ഓട്ടോമാറ്റിക്കായി റൺ ആകുന്ന മെത്തോഡ്; ആരംഭ മൂല്യങ്ങൾ ഇടാൻ. self = ആ ഒബ്ജക്റ്റ്.

```python
class Server:
    def __init__(self, name, port=80):
        self.name = name
        self.port = port

s = Server("web1", 8080)
print(s.name, s.port)   # web1 8080
```

---

## Instance attributes

- **Concept:** Attributes like `self.name` belong to each object (instance). Each object has its own copy.
- **മലയാളം:** ഓരോ ഒബ്ജക്റ്റിനും സ്വന്തം അട്രിബ്യൂട്ടുകൾ; self. ചേർത്ത് എഴുതും.

---

## Methods

- **Concept:** A method is a function inside a class. First parameter is always `self`. Call as `obj.method(args)`.
- **മലയാളം:** ക്ലാസിനുള്ളിലെ ഫങ്ഷൻ; ആദ്യ പാരാമീറ്റർ self. വിളിക്കുമ്പോൾ obj.method().

```python
class Server:
    def __init__(self, name):
        self.name = name
    def status(self):
        return f"Server {self.name} is up"

s = Server("web1")
print(s.status())   # Server web1 is up
```

---

## Class attributes

- **Concept:** A variable defined inside the class but outside methods is shared by all objects. Access as `ClassName.attr` or `self.attr`.
- **മലയാളം:** ക്ലാസിനുള്ളിൽ എഴുതിയ വേരിയബിൾ എല്ലാ ഒബ്ജക്റ്റുകൾക്കും പൊതുവാണ്.

```python
class Server:
    count = 0
    def __init__(self):
        Server.count += 1
```

---

## Inheritance

- **Concept:** A child class can inherit from a parent: `class Child(Parent):`. Child gets all methods/attributes of Parent; can override or add new ones.
- **മലയാളം:** ചൈൽഡ് ക്ലാസ് പാരന്റ് ക്ലാസിന്റെ മെത്തോഡുകളും അട്രിബ്യൂട്ടുകളും പാരായണം ചെയ്യും; മാറ്റാം അല്ലെങ്കിൽ പുതിയത് ചേർക്കാം.

```python
class BaseServer:
    def ping(self):
        return "pong"

class WebServer(BaseServer):
    def ping(self):
        return "web pong"   # override
```

---

## super()

- **Concept:** `super().method()` calls the parent class's version of the method. Useful when extending instead of replacing.
- **മലയാളം:** പാരന്റ് ക്ലാസിന്റെ മെത്തോഡ് വിളിക്കാൻ super() ഉപയോഗിക്കും.

```python
class WebServer(BaseServer):
    def __init__(self, name):
        super().__init__()   # call parent __init__
        self.name = name
```

---

**Next:** **08_exceptions.md** – try/except, error handling.
