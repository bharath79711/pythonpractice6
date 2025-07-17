'''
Branch_name = input("Enter Branch name:")
Loan_amount = int(input("Enter loan amount in lakhs:"))
Land_area = int(input("Enter land area in acres :"))
if Branch_name == 'SBI'and Land_area<10 and Loan_amount<20:
    print("Loan approved in Sbi")
elif Loan_amount<40 and Land_area<20 and Branch_name=='Unionbank':
    print("Loan approved in union bank")

else:
    ("Sorry ! Your not Eligible for loan")
'''
name = input("Enter a name:")
country = input("Enter a country name:")
state = input("Enter a state name:")

if country in name and state in name:
    print(name)
elif (country in name) or (state in name):
    print("yes", name)
else:
    print("country and state  not present")


