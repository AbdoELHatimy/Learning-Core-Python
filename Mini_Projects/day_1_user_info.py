while True:
    try:
        print("-------------- Hello to My Demo Project Python ----------- ")
        
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        city = input("Enter your city: ")
        
        if age < 12:
            print("Sorry, you are a child.") # sorry
        elif age <= 18:
            print("You are a young man.") # text normal
        else:
            print("Hello my brother, you are a man. (Secret text)") # secret text
            
        print(f"Hello and welcome Mr {name}. You are {age} years old, and you live in {city}.")
    
    except ValueError:
        print("Please enter a valid number for age.")
        continue 

    again = input("Do you want to continue? Y/N: ")
    if again.lower() == "n":
        break
