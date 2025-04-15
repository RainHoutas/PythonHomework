
contacts = set()


for i in range(5):
    name = input(f"Enter the name of friend {i + 1}: ")
    phone = input(f"Enter the phone number of {name}: ")
    contacts.add((name, phone))


print("\nPhone Contact List:")
for contact in contacts:
    print(f"Name: {contact[0]}, Phone: {contact[1]}")