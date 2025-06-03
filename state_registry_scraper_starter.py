import requests
from bs4 import BeautifulSoup

def get_registry_info(company_name, state_code):
    if state_code != "AZ":
        return {"error": "Only AZ scraping is implemented for now."}

    search_url = "https://ecorp.azcc.gov/Common/BusinessNameSearch"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }
    payload = {
        "searchTerm": company_name,
        "searchType": "StartsWith",
        "entityType": "All",
        "includePriorName": False
    }

    try:
        response = requests.post(search_url, json=payload, headers=headers)
        response.raise_for_status()
        results = response.json()

        if not results or "entityInfoList" not in results or not results["entityInfoList"]:
            return {"error": "No match found in AZ registry."}

        entity = results["entityInfoList"][0]  # Take the first match

        return {
            "legal_name": entity.get("entityName"),
            "entity_type": entity.get("entityType"),
            "status": entity.get("entityStatusDescription"),
            "address": entity.get("principalAddress"),
            "registered_agent": entity.get("statutoryAgentName")
        }

    except Exception as e:
        return {"error": f"Failed to fetch AZ registry data: {str(e)}"}
