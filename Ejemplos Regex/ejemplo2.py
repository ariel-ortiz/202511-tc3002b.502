import re

texto = "Holá a todos los ITC de este grupo"
m = re.search(r'ITC', texto)
if m:
    print(m.span())
    print(m.string)
    print(m.group())
m = re.search(r'ISC', texto)
if m:
    print(m.span())
    print(m.string)
    print(m.group())
m = re.search(r'I[ST]C', texto)
if m:
    print(m.span())
    print(m.string)
    print(m.group())
m = re.match(r'hola', texto, re.IGNORECASE)
if m:
    print(m.span())
    print(m.string)
    print(m.group())
else:
    print(m)
m = re.fullmatch(r'.*', texto)
if m:
    print(m.span())
    print(m.string)
    print(m.group())

for palabra in re.finditer(r'[a-zá]+', texto, re.IGNORECASE):
    print(palabra.group())
