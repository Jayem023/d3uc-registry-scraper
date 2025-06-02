
import requests
from bs4 import BeautifulSoup

def get_registry_info(company_name, state_code):
    # This is a placeholder URL – in a real scraper, you'd replace it with the state registry URL
    url = f"https://example-registry.com/search?company={company_name}&state={state_code}"

    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch data: {str(e)}"}

    soup = BeautifulSoup(response.text, 'html.parser')

    # Placeholder logic to parse registry info
    result = {
        "legal_name": "Example Legal Name LLC",
        "entity_type": "LLC",
        "status": "Active",
        "address": "123 Example Street, Sample City, ST 12345",
        "registered_agent": "John Doe",
    }

    return result

# Example use
if __name__ == "__main__":
    print(get_registry_info("Acme Inc", "CA"))
