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


def serialize_animal(animal_obj):
    output = ''
    name = animals_data[x]['name']

    # print('type' in animals_data[x]['characteristics'].keys())

    output += f'<li class="cards__item">\n'
    output += f'<div class ="card__title" > {name} </div>\n'

    diet = animals_data[x]['characteristics']['diet']
    output += f"<strong>Diet</strong>: {diet}<br/>\n"

    location = animals_data[x]['locations'][0]
    output += f"<strong>Location</strong>: {location}<br/>\n"

    if 'type' in animals_data[x]['characteristics'].keys() :
        type = animals_data[x]['characteristics']['type']
        output += f"<strong>Type</strong>: {type}<br/>\n"

    output += f" </li>\n"

    return output


animals_data = load_data('animals_data.json')
# print(animals_data)

output = ''  # define an empty string
for x in range(len(animals_data)):
    output += serialize_animal(animals_data)

# Open a file in write mode
with open("output.html", "w") as file:
    file.write(output)