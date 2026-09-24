while True:
    print("\n####################################")
    print("My IT Troubleshooting Knowledgebase:")
    print("1. Network")
    print("2. Windows")
    print("3. Screen")
    print("4. Printer")
    print("Press 0 to exit")

    try:
        choice = int(input("What kind of issue do you have today: "))
    except ValueError:
        print("Please enter a number!")
        choice = 0

    if choice == 0 or choice < 0 or choice > 4:
        break

    if choice == 1:
        pass

    if choice == 2:
        pass

    if choice == 3:
        pass

    if choice == 4:
        pass