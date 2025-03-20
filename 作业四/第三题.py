def seat_position(seat):
    if len(seat) < 2 or not seat[:-1].isdigit() or not seat[-1].isalpha():
        return "Seat number does not exist"

    row = int(seat[:-1])
    col = seat[-1].upper()

    if row < 1 or row > 17:
        return "Seat number does not exist"

    if col in ['A', 'F']:
        return "Window"
    elif col in ['C', 'D']:
        return "Aisle"
    elif col == 'B':
        return "Middle"
    else:
        return "Seat number does not exist"


seat = input("Enter seat number: ")
position = seat_position(seat)
print(position)