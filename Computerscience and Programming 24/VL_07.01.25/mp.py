import requests

def get_material_summary():
    url = "https://api.materialsproject.org/materials/summary/"
    headers = {
        "accept": "application/json",
        "X-API-KEY": "YOU_API_KEY"
    }
    params = {
        "material_ids": "mp-34",
        "deprecated": "false",
        "_per_page": 100,
        "_skip": 0,
        "_limit": 100,
        "_all_fields": "true",
        "license": "BY-C"
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        # Print or process the response JSON
        data = response.json()
        print("Material Summary:", data)
    else:
        # Handle errors
        print(f"Failed to fetch material summary. Status Code: {response.status_code}")
        print(response.text)

# Call the function
if __name__ == "__main__":
    get_material_summary()