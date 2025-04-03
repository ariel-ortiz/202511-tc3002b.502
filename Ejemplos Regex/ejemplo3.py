import re

expreg = r'([aeiou]+)(\d*)|(bond)'
m = re.fullmatch(expreg, 'bond')
if m:
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
else:
    print('No match')

texto = 'una mosca parada en la pared'
print(re.sub(r'[eiou]', 'a', texto))
print(re.sub(r'([aeiou])', r'\1f\1', texto))
