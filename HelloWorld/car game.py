car_input = ""
while car_input != "quit":
    car_input = input("> ").lower()
    if car_input == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit
        """)
    elif car_input == "start":
        print("Car has started")
    elif car_input == "stop":
        print("car has stopped")
    elif car_input == "quit":
        break
    else:
        print("Wrong command entered")

