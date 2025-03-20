def calculate_remaining_trips(total_coal, trips_4t, capacity_4t, capacity_2_5t):
    coal_remaining = total_coal - (trips_4t * capacity_4t)
    trips_needed = coal_remaining / capacity_2_5t
    return trips_needed

total_coal = 29.5
trips_4t = 3
capacity_4t = 4
capacity_2_5t = 2.5

trips_needed = calculate_remaining_trips(total_coal, trips_4t, capacity_4t, capacity_2_5t)
print(f"还需要运送 {trips_needed} 次才能送完")