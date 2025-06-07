# Practical Your Age Full Details


Age = int(input("Your Age: ").strip())
print(type(Age))

months = Age * 12
weeks = Age * 12 * 4
days = Age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"Months: {months}")
print(f"weeks: {weeks:,}")
print(f"days: {days:,}")
print(f"hours: {hours:,}")
print(f"minutes: {minutes:,}")
print(f"seconds: {seconds:,}")