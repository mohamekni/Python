# Loop While


arr = ["Mo" , "RA" , "Ab" , "Sa" , "Kh" , "As"]
x = 0

while x < len(arr) :
    print(f"# {str(x+1).zfill(2)} => {arr[x]}")
    x += 1

else : 
    print("All Friends Printed On Screen")