import re


en = '^[a-zA-Z]*$'
num = '^[0-9]*$'
sc = '^[!@#$%^&*?]*$'

p = re.findall(en, 'abc')
print(p)
