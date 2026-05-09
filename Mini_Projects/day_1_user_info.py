while True:
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        city = input("Enter your city: ")

        print("Hello", name)
        print("You are", age, "years old")
        print("You live in", city)

    except ValueError:
        print("Please enter a valid number for age.")
        continue

    again = input("Do you want to continue? Y/N: ")

    if again.lower() == "n":
        break
