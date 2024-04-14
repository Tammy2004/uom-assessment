import requests
import json

def get_ontology_details(ontology_id):
    """
    Fetches details about the ontology with the given ID from the Ontology Lookup Service API.
    
    Args:
        ontology_id (str): The ID of the ontology.
    
    Returns:
        dict: A dictionary containing the ontology details.
    """
    url = f"http://www.ebi.ac.uk/ols4/api/ontologies/{ontology_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        ontology_data = response.json()
        return {
            "title": ontology_data["config"]["title"],
            "description": ontology_data["config"]["description"],
            "number_of_terms": ontology_data["numberOfTerms"],
            "status": ontology_data["status"]
        }
    else:
        return None

def print_human_details(details):
    """
    Prints the ontology details in a human-readable format.
    
    Args:
        details (dict): A dictionary containing the ontology details.
    """
    if details:
        print("Title:", details["title"])
        print("Description:", details["description"])
        print("Number of terms:", details["number_of_terms"])
        print("Status:", details["status"])
    else:
        print("Failed to fetch ontology details.")

def print_machine_details(details):
    """
    Prints the ontology details in a machine-readable JSON format.
    
    Args:
        details (dict): A dictionary containing the ontology details.
    """
    if details:
        print(json.dumps(details, indent=2))
    else:
        print("{}")

if __name__ == "__main__":
        
    flag = True
 
 
    # details = {}

    # loop to check if the input ontology id is valid or not
    while flag:
       
       # input ontology id
        ontology_id = input("Please enter a valid ontology ID:")

        # retrieve ontology details
        details = get_ontology_details(ontology_id)

        # validate the ontology id 
        if details: 
            print("What type of output do you want? (Pick either 1 or 2)")
            print("1. Machine readable\n2. Human readable")
            output_type = input()
            print()

            #print the details in the desired format
            if output_type == "1":
                print_machine_details(details)
                flag = False

            elif output_type == "2":
                print_human_details(details)
                flag = False

            else:
                print("Invalid input. Please enter a valid input.")
        # if the ontology id is invalid, prompt the user to enter a valid ontology id
        elif details is None:
            continue

