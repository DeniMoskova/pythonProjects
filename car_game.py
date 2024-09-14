command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Already started!")
        else:
            started = True
        print("Ready GO!")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("start - the car starts\nstop - the car stops\nquit - the game ends.")
    elif command == "quit":
        print("Bye!")
        break
    else:
        print("I don't understand?")
