car_input = ""
car_status = False
while car_input != "quit":
    car_input = input("> ").lower()
    if car_input == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit
        """)
    elif car_input == "start":
        if car_status:
            print("Car has already started")
        else:
            print("Car has started")
            car_status = True
    elif car_input == "stop":
        if car_status:
            print("car has stopped")
            car_status = False
        else:
            print("Car is already stopped")
    elif car_input == "quit":
        break
    else:
        print("Wrong command entered")

