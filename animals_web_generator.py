from colorama import Fore, Back, Style, init
# Initialize colorama
init()
# # Print colored text
# print(Fore.RED + "This is red text.")
# print(Fore.GREEN + "This is green text.")
# print(Back.YELLOW + "This text has a yellow background.")
# print(Style.BRIGHT + "This is bright text.")
# print(Style.RESET_ALL + "This resets all styles.")
print(Fore.BLACK + Back.YELLOW + Style.BRIGHT)
# ----- above for colors --------------------

import json

def load_data(file_path):
  """ Loads a JSON file """
  with open("animals_data.json", "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')


output = ''  # define an empty string
for x in range(len(animals_data)):
    name = animals_data[x]['name']
    location = animals_data[x]['locations'][0]
    diet = animals_data[0]['characteristics']['diet']
    type = animals_data[0]['characteristics']['type']
    output +=  f"Name: {name}\n"
    output += f"Location: {location}\n"
    output += f"Diet: {diet}\n"
    output += f"Type: {type}\n"

# print(output)



# Open a file in write mode
with open("output.html", "w") as file:
    file.write(output)