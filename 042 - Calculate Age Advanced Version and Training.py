# Calculate Age Advanced Version and Training



# Write Note
print("#" * 80)
print("You Can Write The First Letter Or Full Name Of The Time Unit".center(80,"#"))
print("#" * 80)


# Collect Age Data
Age = int(input("Your Age :").strip())
# Collect Time Unit Data
unit = input("Choose Time Unit : months, Weeks, Days? :").strip().lower()

if unit == "days" or unit =="d":

    print("You Choosed Days")
    print(f"You Lived For {Age * 365} Days")

elif unit == "Weeks" or unit =="w":

    print("You Choosed Weeks")
    print(f"You Lived {Age * 12 * 4} Weeks")

elif  unit == "months" or unit =="m":

    print("You Choosed Months")
    print(f"You Lived {Age * 12} Months")