import requests
import json


# extract the needed values

flag = True

while flag:
        
    # ask for user input below this line
    print("Please enter a valid ontology ID:")
    ontology_id = input()

    # Construct the URL with the user input
    url = f"http://www.ebi.ac.uk/ols4/api/ontologies/{ontology_id}"

    # Make a GET request to the API
    response = requests.get(url)

    if response.status_code == 200:
        flag = False
    else:
        continue

ontology_title = response.json()["config"]["title"]
ontology_description = response.json()["config"]["description"]
num_terms = response.json()["numberOfTerms"]
status = response.json()["status"]

flag = True 

while flag:
    print("What type of output do you want?")
    print("1. Machine readable\n2. Human readable")
    output_type = input()
    print()

    if output_type == "1":

        output = {
            "title": ontology_title,
            "description": ontology_description,
            "number_of_terms": num_terms,
            "status": status
        }
        print(json.dumps(output, indent = 2))
        flag = False

    elif output_type == "2":
        print("Title:", ontology_title)
        print("Description:", ontology_description)
        print("Number of terms:", num_terms)
        print("Status:", status)
        flag = False

    else:

        print("Invalid input. Please enter a valid input.")


