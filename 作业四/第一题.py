def calculate_party_fee(salary):
    if salary <= 3000:
        fee = salary * 0.005
    elif salary <= 5000:
        fee = salary * 0.01
    elif salary <= 10000:
        fee = salary * 0.015
    else:
        fee = salary * 0.02
    return fee

salary = float(input("Enter your salary: "))
fee = calculate_party_fee(salary)
print(f"The party fee is: {fee:.2f} yuan")