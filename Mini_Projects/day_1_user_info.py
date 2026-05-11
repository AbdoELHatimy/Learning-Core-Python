# Define a function to collect user information
def get_user_info():
    # Ask for the user's name
    name = input("Enter your name: ")
    # Ask for the user's age and convert it to an integer
    age = int(input("Enter your age: "))
    # Ask for the user's city
    city = input("Enter your city: ")
    # Return the collected information
    return name, age, city

# Main program loop
while True:
    try:
        print (" ________ Hello to My Demo proji python _______")
        
        # Call the function to get user information
        name, age, city = get_user_info()
        
        # Display the user's information
        print(f"Hello, {name}. You are {age} years old and live in {city}.")
        
        # Check if the user is young or an adult
        if age < 18:
            print("Sorry, you are young.")
        else:
            print("Welcome, brother!")
            
    except ValueError:
        # Handle the error if the user enters a non-numeric value for age
        print("Please enter a valid age.")
        # Go back to the beginning of the try block
        continue

    # Ask the user if they want to continue
    again = input("Continue? (y/n): ")
    # If the user enters 'n', exit the loop
    if again == "n":
        break
