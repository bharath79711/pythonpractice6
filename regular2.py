import re

x="""
  chintakunta village cvapb4576m 133a1a0326 12345 10f65a0306 19w55a0406
   thiru122mala@gmail.com anu@outlook.com bharath70@gmail.com kadapa
   516172 516175 517351  838535965466 940244665036

"""
data_mails=re.findall("\w{1,}@[a-zA-z]{1,}.com",x)

print(data_mails)


data_rolls = re.findall("\d{1,}[a-zA-Z]\d{1,}[a-zA-Z]\d{4}",x)
print(data_rolls)

data_adhar_no = re.findall("\d{12}",x)
print(data_adhar_no)