import requests

class IncognitonAPI:
    def __init__(self, api_endpoint):
        self.api_endpoint = api_endpoint
    
    def create_profile(self, username, password, **kwargs):
        """Creates a profile in Incogniton."""
        payload = {
            "username": username,
            "password": password,
            **kwargs
        }
        response = requests.post(f"{self.api_endpoint}/create", json=payload)
        return response.json()
    
    def open_profile(self, profile_id):
        """Opens an existing profile in Incogniton."""
        response = requests.get(f"{self.api_endpoint}/open/{profile_id}")
        return response.json()
    
    def add_profile(self, source_data):
        """Adds/imports a profile in Incogniton."""
        response = requests.post(f"{self.api_endpoint}/add", json=source_data)
        return response.json()
    
    def delete_profile(self, profile_id):
        """Deletes a profile in Incogniton."""
        response = requests.delete(f"{self.api_endpoint}/delete/{profile_id}")
        return response.json()
    
    def edit_profile(self, profile_id, updated_data):
        """Edits a profile in Incogniton."""
        response = requests.put(f"{self.api_endpoint}/edit/{profile_id}", json=updated_data)
        return response.json()
 
