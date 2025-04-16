import requests
import json
import time
import os
from typing import Dict, Any, Optional


class STJClient:
    """
    A client for interacting with the STJ API that requires token authentication.
    """
    
    # Fixed API endpoints
    AUTH_URL = "https://cpe.web.stj.jus.br/api/auth/withoutRecapcha"
    CONSULTA_URL = "https://cpe.web.stj.jus.br/api/consultaInteligente"
    
    def __init__(self, username: str, password: str):
        """
        Initialize the API client with credentials.
        
        Args:
            username: Username for authentication
            password: Password for authentication
        """
        self.username = username
        self.password = password
        self.token = None
        self.token_expiry = 0  # Timestamp when token expires
        
    def authenticate(self) -> bool:
        """
        Authenticate with the API using the fixed auth URL and obtain a token.
        
        Returns:
            bool: True if authentication was successful, False otherwise
        """        
        payload = {
            "username": self.username,
            "password": self.password
        }
        
        try:
            response = requests.post(self.AUTH_URL, json=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            data = response.json()
            self.token = data.get("token")
            
            # self.token_expiry = time.time() + data.get("expires_in", 3600)
            self.token_expiry = time.time() + 3600  # Default: 1 hour expiry
            
            return True
        except requests.exceptions.RequestException as e:
            print(f"Authentication failed: {e}")
            return False
    
    def ensure_authenticated(self) -> bool:
        """
        Ensure the client has a valid authentication token.
        
        Returns:
            bool: True if a valid token exists or was obtained, False otherwise
        """
        # Check if token exists and is not expired
        if self.token is None or time.time() >= self.token_expiry:
            return self.authenticate()
        return True
    
    def get_headers(self) -> Dict[str, str]:
        """
        Get headers for API requests including the authentication token.
        
        Returns:
            Dict[str, str]: Headers dictionary
        """
        return {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }
    
    def save_to_file(self, data: Any, save_dir: str, filename: str) -> str:
        """
        Save data to a JSON file on disk.
        
        Args:
            data: Data to save (must be JSON serializable)
            save_dir: Directory to save the file in
            filename: Name of the file (without path or extension)
            
        Returns:
            str: Full path to the saved file
        """
        # Create full path
        filepath = f'{save_dir}/{filename}'
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Save data to file with nice formatting
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        return filepath
    
    def load_from_file(self, save_dir: str, filename: str) -> Any:
        """
        Load data from a saved JSON file.
        
        Args:
            save_dir: Directory where the file is saved
            filename: Name of the file (without path, with or without .json extension)
            
        Returns:
            Any: The loaded JSON data
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            json.JSONDecodeError: If the file contains invalid JSON
        """
        # Ensure filename has .json extension
        if not filename.endswith('.json'):
            filename += '.json'
            
        # Create full path
        filepath = f'{save_dir}/{filename}'
        
        # Load data from file
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def validate_processo_numero(self, num_processo: str) -> bool:
        """
        Validate the processo number format.
        
        Args:
            num_processo: Process number to validate
            
        Returns:
            bool: True if the format appears valid, False otherwise
        """
        # This is a simplified validation
        # In a real implementation, you might want to check against expected patterns
        if not num_processo or len(num_processo.strip()) < 5:
            return False
        return True

    def consultar_processo(self, num_processo: str, save: bool = False, save_dir: Optional[str] = ".") -> Dict[str, Any]:
        """
        Make a GET request to the API to consult a process.
        
        Args:
            num_processo: classe numero, numero origem, numero unico ou registro
            save: Whether to save the response to a file
            save_dir: Directory to save response files in
            
        Returns:
            Dict[str, Any]: JSON response from the API
            
        Raises:
            Exception: If authentication fails or the API request fails
            ValueError: If the processo number format is invalid
        """
        # Validate the processo number
        if not self.validate_processo_numero(num_processo):
            raise ValueError(f"Invalid processo number format: {num_processo}")
            
        if not self.ensure_authenticated():
            raise Exception("Failed to authenticate with the API")
        
        url = f"{self.CONSULTA_URL}/{num_processo}"
        
        try:
            response = requests.get(url, headers=self.get_headers())
            response.raise_for_status()
            data = response.json()
            
            # Save to file if requested
            if save:
                filename = f"{''.join(filter(str.isalnum, num_processo))}_time_{int(time.time())}.json"
                saved_path = self.save_to_file(data, save_dir, filename)
                print(f"Response saved to: {saved_path}")

            else: 
                return data

        except requests.exceptions.RequestException as e:
            # Handle specific error cases (e.g., 401 for token expiry)
            if hasattr(e, 'response') and e.response is not None and e.response.status_code == 401:
                # Token might have expired, try to re-authenticate
                if self.authenticate():
                    # Retry the request with the new token
                    response = requests.get(url, headers=self.get_headers())
                    response.raise_for_status()
                    data = response.json()
                    
                    # Save to file if requested
                    if save:
                        filename = f"{''.join(filter(str.isalnum, num_processo))}_time_{int(time.time())}.json"
                        saved_path = self.save_to_file(data, save_dir, filename)
                        print(f"Response saved to: {saved_path}")
                        
                    return data
            
            # Re-raise the exception with more context
            raise Exception(f"Error consulting processo {num_processo}: {str(e)}") from e

