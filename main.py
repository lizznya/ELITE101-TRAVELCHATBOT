
program_loop = True
def display_main_menu():
    print("1. Christmas in London")
    print("2. Christmas in Paris")
    print("3. Christmas in Sweeden")
    print("4. I'm not interested in any of them")

name = 'user'
name = input("Welcome to the Traveler official chatbot!, \nWhat is your name?")

try:
    age = int(input(f"Hello {name}!, How old are you?"))
except ValueError:
    print ("Please enter a valid number for your age.")
    program_loop = False
    age = 0

if age < 18:
    print("Sorry, you are not old enough to use this chatbot")
    program_loop = False
else:
    print(f"{name}, that's a great age to travel!, These are our best deals today")
    display_main_menu()
    user_choice = int(input("Enter a number between 1-4: "))
    if user_choice == 1:
        print("You have selected Christmas in London :D!")
        print("The travel is from December 20 to January 2")
        print("The price for this trip is $6k")
        choice = input("Are you interested in this trip?")
        if choice.lower() == 'yes':
            print("Great! We will send you more information about this trip")
        elif choice.lower == 'no':
            print("Okay, we will send you back to the main menu")
            display_main_menu()
    elif user_choice == '2':
        print("You're traveling to the city of love and on Christmas season!")
        print("The travel is from December 20 to January 2")
        print("The price for this trip is $7k")
        choice = input("Are you interested in this trip?")
        if choice.lower == 'yes':
            print("Great! We will send you more information about this trip")
        elif choice.lower == 'no':
            print("Okay, we will send you back to the main menu")
            display_main_menu()
    elif user_choice == '3':
        print(f"You're travelling to the land of snow, a wise decision {name}!")
        print("The travel is from December 20 to January 2")
        print("The price for this trip is $8k")
        choice = input("Are you interested in this trip?")
        if choice.lower == 'yes':
            print("Great! We will send you more information about this trip")
        elif choice.lower == 'no':
            print("Okay, we will send you back to the main menu")
            display_main_menu()
    elif user_choice == '4':
        print("It was nice to meet you {name}!, thank you for using the chatbot")
        in_use = False
            


