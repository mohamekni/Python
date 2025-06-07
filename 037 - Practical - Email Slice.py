# Practical Slice Email


name = "Mohamed Mekni".strip().capitalize()
Email = "mohamed.MEKNI@esprit.com".strip()
print(Email[0:Email.index('@')]) # mohamed.MEKNI

userName = Email[:Email.index('@')]
domain = Email[Email.index('@') + 1:]
print(f"Your UserName Is {userName} and Your Domain Is {domain}") # Your UserName Is mohamed.MEKNI and Your Domain Is esprit.com