import re
"""
x="India is my Country . Bharath lives in Banglore with Tiru and Anu"

data=re.findall("[A-Z][a-zA-Z]{1,}",x)
print(data)
"""
"""
x="Today's date is 13-07-2025. My DOB is 02-11-1996 in valid:1-1-1999"

data= re.findall("\d{2}-\d{2}-\d{4}",x)
print(data)
"""
"""
x="I am learning python and enjoying building and debbuing programs"

data = re.findall("[a-zA-Z]{1,}ing",x)
print(data)
data1= re.findall("\w{1,}ing",x)
print(data1)
"""
"""

x="python is easy. pycharm is IDE.I like pygame and pyinstaller."

data=re.findall("py\w{1,}",x)
print(data)
"""
x= "cvapb4576m  133a1a0326  10f65a0306 abcd xyz abc123"

data=re.findall("\w{1,}\d{1,}\w",x)


print(data)



