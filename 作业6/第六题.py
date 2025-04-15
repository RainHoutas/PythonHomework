
trains = [
    {"train_no": "G101", "departure": "Beijing", "arrival": "Tianjin", "time": "08:00"},
    {"train_no": "G102", "departure": "Beijing", "arrival": "Tianjin", "time": "09:00"},
    {"train_no": "G103", "departure": "Beijing", "arrival": "Tianjin", "time": "10:00"},
    {"train_no": "G104", "departure": "Beijing", "arrival": "Tianjin", "time": "11:00"}
]

print("Available trains from Beijing to Tianjin:")
print("Train No. | Departure | Arrival | Time")
for train in trains:
    print(f"{train['train_no']}      | {train['departure']}     | {train['arrival']}   | {train['time']}")


selected_train = input("\nEnter the train number you want to book: ")


train_found = next((train for train in trains if train["train_no"] == selected_train), None)

if train_found:
    print(f"\nYou have successfully booked Train {train_found['train_no']} from {train_found['departure']} to {train_found['arrival']} at {train_found['time']}.")
    print("Please proceed to the station for boarding.")
else:
    print("\nInvalid train number. Please try again.")