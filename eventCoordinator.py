# script.py

guests = {}

# Step 1: Modify read_guestlist function to be a generator
def read_guestlist(file_name):
    text_file = open(file_name, 'r')
    while True:
        line_data = text_file.readline().strip().split(",")
        if len(line_data) < 2:
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        yield name  # Yield each guest name
        guests[name] = age

# Step 2: Add another guest, Jane (35)
read_guestlist_generator = read_guestlist("guest_list.txt")
next(read_guestlist_generator)
read_guestlist_generator.send("Jane,35")

# Step 3: Finish yielding the rest of the names
for guest_name in read_guestlist_generator:
    print(guest_name)

# Step 4: Define a generator expression for guests aged 21 and over
over_21_generator = (name for name, age in guests.items() if age >= 21)
for guest_name in over_21_generator:
    print(guest_name)

# Step 5: Create 3 separate generator functions for each table
def table_generator(table_number, food_list):
    for seat_number in range(1, 6):
        yield ("Food Name", f"Table {table_number}", f"Seat {seat_number}")

table_1 = table_generator(1, ["Chicken", "Beef", "Fish"])
table_2 = table_generator(2, ["Chicken", "Beef", "Fish"])
table_3 = table_generator(3, ["Chicken", "Beef", "Fish"])

# Step 6: Create a generator function to assign meals to guests
def assign_meal(guests, seating_generator):
    for guest_name in guests:
        yield (guest_name, next(seating_generator))

# Example usage
for guest_and_meal in assign_meal(guests.keys(), table_1):
    print(guest_and_meal)

# Congratulations, you were able to successfully plan and coordinate your first event!
