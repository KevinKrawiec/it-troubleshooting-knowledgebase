import json

def show_knowledgebase(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    for title, steps in data.items():
        print(f"\n{title}")

        for step in steps:
            print(f"- {step}")


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

    if choice == 0:
        break

    elif choice == 1:
        show_knowledgebase("network.json")

    elif choice == 2:
        show_knowledgebase("windows.json")

    elif choice == 3:
        show_knowledgebase("screen.json")

    elif choice == 4:
        pass

    else:
        print("Wrong number, try again.")