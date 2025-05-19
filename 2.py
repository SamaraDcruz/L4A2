# Ask the user for the amount
amount = int(input("Enter the amount: "))

# Count the number of each note
note2000 = amount // 2000
amount = amount % 2000

note500 = amount // 500
amount = amount % 500

note100 = amount // 100
amount = amount % 100

# Show the result
print("Notes needed: ")
print("2000:", note2000)
print("500:", note500)
print("100:", note100)

# Show if anything is left
if amount > 0:
    print("Leftover amount that can't be converted into notes:",
     amount)