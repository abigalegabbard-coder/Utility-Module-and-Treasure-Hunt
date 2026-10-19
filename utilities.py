import os
import time

def getNonEmptyString(prompt):
    """Rejects empty/whitespace only input, and returns the trimmed string"""
    while True:
        user_resp = input(prompt).strip().title()
        if user_resp == "":
            print("Enter something next time")
        else:
            return user_resp

def printNumberedList(items):
    """Print items numbered from 1, or a message if empty."""
    if len(items) == 0:
        print("No items to display.")
    else:
        number = 1
        for item in items:
            print(f"{number}. {item}")
            number += 1

def getValidInt(prompt, min=0, max=100):
    """Get an integer within the inclusive minimum and maximum range."""
    while True:
        user_response = input(prompt).strip()
        if user_response.isdigit():
            user_number = int(user_response)
            if min <= user_number <= max:
                    return int(user_response)
            else:
                print(f"Invalid")
                user_response = input(prompt).strip()
        else:
            print("Invalid input. Please enter a whole number.")
            user_response = input(prompt).strip()

def clearScreen():
    """Clear the window's console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(message = "Press enter to continue..."):
    """Shows the message and wait for enter"""
    input(message)


def getValidResponse(prompt, validResponses):
    """Get an accepted response, ignoring case and spaces."""
    valid_responses = [response.lower().strip() for response in validResponses]
    while True:
        response = input(prompt).strip().lower()
        if response == "y":
            pass
        elif response == "n":
            clearScreen()
            break
        else:
            print("Enter one of the given responses.")


def filterByLength(items, minLength, maxLength):
    """Returns strings with the lengths in the inclusive range, preserving order"""
    return [item for item in items if minLength <= len(item) <= maxLength]

def analyzeNumbers(numbers):
    """Return positive numbers and positive, negative, and zero counts."""
    positive_numbers = [number for number in numbers if number > 0]
    positive_count = len(positive_numbers)
    negative_count = len([number for number in numbers if number < 0])
    zero_count = len([number for number in numbers if number == 0])
    return positive_numbers, positive_count, negative_count, zero_count

def main():
    """Gathers everything together"""
    pause(message="Press enter to continue...")
    getNonEmptyString("Enter your name: ")
    printNumberedList([])
    getValidInt("Enter your choice (1-3): ", min=0, max=100)
    analyzeNumbers()
    getValidResponse("Enter an y to continue, or n to quit: ", validResponses=["y","n"])

if __name__ == "__main__":
    main()