name, char=input("enter your name and char: \t").split(",")

print(f"length of your name is :{len(name)}")
print(f"character count : {name.lower().count(char.lower())}")

name, char=input("enter your name and char: \t").split(",")

print(f"length of your name is :{len(name)}")
print(f"chracter count {name.strip().lower().count(char.strip().lower())}")

# "kunal"---------> "harshit" -------> "harshit"


