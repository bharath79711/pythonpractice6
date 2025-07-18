import re

x="Bharath is learning python Bharath is hard working and Bharath is good"

try:
 data=re.match("Bharath",x)
except Exception as error:
            print("error is:",error)
print(data)
print (data.group())


data1=re.search("Bharath",x)
print(data1)
print(data1.group())


data2=re.findall("Bharath",x)
print(data2)


data3 =  re.sub("Bharath","Tiru",x)
print(data3)
