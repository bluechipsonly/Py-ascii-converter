import re
import os
import time as t
import sys as s

from regex_load import regex_param as r
from system_load import sys_param


# Shows user who they are
output = os.popen("whoami").read()
print(f"Current user: {output.strip()}")

# menu displays
def select_menu():
    while True:
        print("\nASCII Converter")
        print("[1] Convert Text to ASCII")
        print("[2] Convert ASCII to Text")
        print("[3] Exit")

        choice = input("Make a selection: ").strip()

        try:
            choice = int(choice)  # Convert input to integer
            
            if choice in range(1, 4):  # Valid choices are 1, 2, or 3
                ascii_convert.main(choice)  # Calls main() function once with the selected choice
            else:
                print("\nInvalid selection! Please enter 1, 2, or 3.")

        except ValueError:
            print("\nInvalid input! Please enter a number.")
        except Exception as e:
            print(f"\n Invalid choice, check the syntax at: {e}")

# Calls select menu function and regex-load and sys-load function
# Along with ASCII pattern functions


class ascii_convert:
    @staticmethod
    def main(choice):
        """ Processes menu selection based on choice """
        if choice == 1:
            text_char = input("Enter the plaintext you would like to encode: ").strip()
            if not re.match(r"^[\S\s]+$", text_char):
                print("INVALID TEXT, cannot encode.. New lines are not allowed")
            else:
                r() # Calls function from regex_load.py
                ascii_output = ascii_convert.text_to_ascii(text_char)
                sys_param() # Calls function from system_load.py
                print(f"ASCII Output: {ascii_output}")
                t.sleep(0.1)

        elif choice == 2:
            text_char = input("Enter ASCII numbers to convert to plaintext: ").strip()
            if not re.match(r"^\d+( \d+)*$", text_char):
                print("INVALID INPUT: Only numbers and spaces allowed (e.g., '72 101 108 108 111')")
            else:
                r()
                text_output = ascii_convert.ascii_to_text(text_char)
                sys_param()
                print(f"Plaintext Output: {text_output}")
                t.sleep(0.1)

        elif choice == 3:
            r() # Called function from regex.py
            print("Exiting program . . . ")
            t.sleep(0.1)
            exit()

    @staticmethod
    def text_to_ascii(text):
        """ Converts text to ASCII codes (space-separated). """
        return " ".join(str(ord(char)) for char in text)

    @staticmethod
    def ascii_to_text(ascii_str):
        """ Converts ASCII codes (space-separated) back to text. """
        try:
            return "".join(chr(int(num)) for num in ascii_str.split())
        except ValueError:
            return "Invalid ASCII input!"

# Run the menu

if __name__ == "__main__":
    select_menu()
