#src/models.py
"""
Module: models.py
Purpose: Defines the Credential and Vault classes for the CLI Password Manager.
"""

class Credential:
    """Represents a single credential entry.

    Args:
        site (str): The name of the website or service.
        username (str): The username associated with the credential.
        password (str): The password associated with the credential.
    """

    def __init__(self, site: str, username: str, password: str):
        self.site = site
        self.username = username
        self.password = password

    def to_dict(self) -> dict:
        """Convert credential to dictionary format.

        Returns:
            dict: Dictionary containing site, username, and password.
        """
        return {
            "site": self.site, 
            "username": self.username, 
            "password": self.password
        }

class Vault:
    """Manages a collection of credentials."""

    def __init__(self):
        self.credentials = []

    def add(self, credential: Credential):
        """Add a new credential to the vault.

        Args:
            credential (Credential): The credential object to add.
        """
        self.credentials.append(credential)

    def list_all(self):
        """Return all stored credentials.

        Returns:
            list[Credential]: List of all credentials in the vault.
        """
        return self.credentials

    def find(self, site: str):
        """Search for credentials by site name.

        Args:
            site (str): The site name to search for.

        Returns:
            list[Credential]: List of credentials matching the site name.
        """
        return [c for c in self.credentials if c.site.lower() == site.lower()]
