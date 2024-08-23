import requests
import json

protein_list = input("Proteins you are searching for (separated by commas): ")
protein_names = [name.strip() for name in protein_list.split(',')]
ion = input("Ion you want to add: ")

def search_uniprot(protein_name):
    query = f'{protein_name.replace(" ", "+")}'
    url = f'https://rest.uniprot.org/uniprotkb/search?query={query}%28LENGTH%3A%5B273+TO+1818%5D%29+AND+%28taxonomy_id%3A10090%29&format=json'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        sequences = []

        results = data.get('results', [])
        if not results:
            print(f"No results found for {protein_name}.")
            return None

        for result in results:
            if result['primaryAccession'] == protein_name:
                sequence_info = result.get('sequence', {})
                sequence = sequence_info.get('value', 'No sequence available') if sequence_info else 'No sequence available'

                sequences.append({
                    "proteinChain": {
                        "sequence": sequence,
                        "glycans": [],
                        "modifications": [],
                        "count": 1
                    }
                })

        return sequences
    else:
        print(f"Status code error: {response.status_code}")
        return None

file_name = 
output_data = {
    "name": protein_list,
    "modelSeeds": [],
    "sequences": []  
}

for name in protein_names:
    result = search_uniprot(name)
    if result:
        output_data["sequences"].extend(result)

if ion:
    ion_entry = {
        "ion": ion,
        "count": 1
    }
    output_data["ion"] = ion_entry 

output_file = "protein_search_results.json"
with open(output_file, 'w') as f:
    json.dump([output_data], f, indent=4) 

print(f"Results saved to {output_file}")
