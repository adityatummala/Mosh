i = 0
lucky_number = 10
is_lucky = False
while i < 3:
    guess_number = int(input("Enter the lucky number: "))
    i += 1;
    if guess_number == lucky_number:
        print("You found the lucky number. Congrats!")
        is_lucky = True
        break
    else:
        print("That's not right! \n")
if not is_lucky:
    print("\n You have exhausted your chances. Bye!")

