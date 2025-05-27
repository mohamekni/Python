# Strings Methods


# replace(old, new, count)
a = "one two three one one two two three three"
print(a.replace("one", "1"))    # 1 two three 1 1 two two three three
print(a.replace("one", "1", 1)) # 1 two three one one two two three three
print(a.replace("one", "1", 2)) # 1 two three 1 one two two three three


# join(Iterable)
myList = ["Mohamed" , "Rahma" , "Ademo"]
print("-".join(myList)) # Mohamed | Rahma | Ademo
print(",".join(myList)) # Mohamed , Rahma , Ademo
print(type("/".join(myList))) # str
