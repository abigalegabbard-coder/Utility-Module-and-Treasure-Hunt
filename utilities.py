import os
import time


def get_non_empty_string(prompt):
    """Rejects empty/whitespace only input, and returns the trimmed string"""
    while True:
        user_resp = input(prompt).strip()
        if user_resp == "":
            print("Enter something next time")
        else:
            return user_resp

def print_numbered_list(items):
    """Prints items numbered from 1, for an empty list, print 'no items to display'"""
    return 

def get_valid_int(prompt, min=0, max=100):
    """Repeats until a valid integer within the range is entered, and returns the integer"""
    if prompt == 1:
        pass
    elif prompt == 2:
        pass
    elif prompt == 3:
        pass

def clear_screen():
    """Clear the window's console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(message = input("Press enter to continue...")):
    """Shows the message and wait for enter"""
    #make it show the message
    if message == "":
        time.sleep(1.5)


def get_valid_response(prompt, validResponses):
    """Repeats until an accepted responce is entered, ignores case and surrounding spaces, and returns the lowercase input"""
    #add in main for it to give it back in lowercase, and then also make the prompt an input and make it ask for whatever
    while True:
        resp = input(prompt).strip().lower()
        if resp in validResponses: #if resp in validResponses
            return resp
        else:
            print("Enter a given response")

def filter_by_length(items, minLength, maxLength):
    """Uses list comprehension to return strinfs with lengths in the inclusive range, preserving order"""
    pass

def analyze_numbers(numbers):
    """
    Uses list comprehension to collect positive numbers. 
    Return four values: positive-number list, positive count, negative count, zero count
    """
    pass

def main():
    get_valid_int(prompt, min=0, max=100)
    get_valid_response("Enter an y to continue, or n to quit: ", validResponses=["y","n"])
    get_non_empty_string("Enter your name: ")
    clear_screen()
    pause(message="Press enter to continue...")
    print_numbered_list(items)

if __name__ == "__main__":
    main()