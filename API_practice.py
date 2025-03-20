#Task 2 printing out competition names
import requests
import json
response = requests.get ("http://api.football-data.org/v4/competitions/")
response.status_code
data = response.json()
print (data)

our_focus = data["competitions"]
competition_names_list = []

for details in our_focus:
    details_dict= details
    competition_names = (details["name"])
    competition_names_list.append(competition_names)

print (competition_names_list)

#Task 3.1 Extracting female details and male details into 2 seperate lists
import requests
import json
url = "https://randomuser.me/api/?results=500"
response = requests.get(url)
response.status_code
data = response.json()
our_focus_dictionary = data['results']
female_details = []
male_details = []
date_of_birth = []
first_name = []
last_name = []
full_name = []


for details in our_focus_dictionary:
    if details["gender"] == "female":
        female_details.append(details)
    elif details["gender"] == "male":
        male_details.append(details)

print (female_details)
print (male_details)


#Task 3.2 Extracting date of birth into a list
for details in our_focus_dictionary:
    date_of_birth.append(details["dob"]["date"])
print (date_of_birth)


#Task 3.3 Extracting first and last name and concatenating it in a list
for details in our_focus_dictionary:
    first_name.append(details["name"]["first"])
print (first_name)

for details in our_focus_dictionary:
     last_name.append(details["name"]["last"])
print (last_name)

