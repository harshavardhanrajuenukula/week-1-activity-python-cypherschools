winning_number = 27
user_input = int(input(""))
if user_input ==winning_number:
    print("YOU WIN!!")
else:
    if user_input < winning_number:
        print("too low")
    else:
        print("too high")