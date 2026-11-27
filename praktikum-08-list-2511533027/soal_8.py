number_of_rows = 4
seats_per_row = 5
# Write your code below
seats = [["."] * seats_per_row for _ in range(number_of_rows)]

while True:
  for r in range(number_of_rows):
    print(f"Row {r + 1}: {' '.join(seats[r])}")

  row_input = int(input("Row (0 to stop): "))
  if row_input == 0:
    break

  seat_input = int(input("Seat: "))

  if not (1 <= row_input <= number_of_rows) or not (
      1 <= seat_input <= seats_per_row
  ):
    print("Invalid seat.")
  elif seats[row_input - 1][seat_input - 1] == "X":
    print("Seat already taken.")
  else:
    seats[row_input - 1][seat_input - 1] = "X"
    print("Seat booked.")

taken_count = 0
for row in seats:
  for seat in row:
    if seat == "X":
      taken_count += 1

print(f"Seats taken: {taken_count}")