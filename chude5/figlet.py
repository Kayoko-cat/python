
import pyfiglet

text = input("Input: ")
font = input("Font: ")

try:
    result = pyfiglet.figlet_format(text, font=font)
    print(result, end="")
except pyfiglet.FontNotFound:
    print("Invalid usage")
