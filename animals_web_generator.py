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

"""
Name
Diet
The first location from the locations list
Type


Example output

Name: American Foxhound
Diet: Omnivore
Location: North-America
Type: Hound

Name: Arctic Fox
Diet: Carnivore
Location: Eurasia
Type: Mammal

Name: Cross Fox
Diet: Carnivore
Location: North-America
Type: mammal


"""


"""
for animal_data in data:
    print(f"Name: {animal_data['name']}")
    print(f"Diet: {animal_data['characteristics']['diet']}")
    
    
    

output = ''  # define an empty string
for animal_data in data:
    # append information to each string
    output += f"Name: {animal_data['name']}\n"
    output += f"Diet: {animal_data['characteristics']['diet']}\n"
    ...
print(output)
    
"""




test = {
    "name": "American Foxhound",
    "taxonomy": {
      "kingdom": "Animalia",
      "scientific_name": "Canis lupus"
    },
    "locations": [
      "North-America"
    ],
    "characteristics": {
      "diet": "Omnivore",
      "type": "Hound",
    }
  },

# print(test[0]['name'])
# print(test[0]['locations'][0])
# print(test[0]['characteristics']['diet'])
# print(test[0]['characteristics']['type'])


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

print(output)

#
# for animal_data in data:
#     # append information to each string
#     output += f"Name: {animal_data['name']}\n"
#     output += f"Diet: {animal_data['characteristics']['diet']}\n"
#     ...
# print(output)
#


# Open a file in write mode
with open("output_animals.html", "w") as file:
    file.write(output)