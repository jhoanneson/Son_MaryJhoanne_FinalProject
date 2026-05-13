#src/storage.py
"""
Module: storage.py
Purpose: Handles encryption and persistence of credentials using Fernet.
"""

import json
import os
from cryptography.fernet import Fernet
from models import Credential, Vault

DATA_DIR = "data"
KEY_FILE = os.path.join(DATA_DIR, "key.key")
VAULT_FILE = os.path.join(DATA_DIR, "vault.json")


class StorageManager:
    """Handles encrypted storage of credentials."""

    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        self.key = self._load_or_create_key()
        self.cipher = Fernet(self.key)

    def _load_or_create_key(self):
        """Load encryption key or create a new one.

        Returns
        bytes
            The encryption key.
        """
        if not os.path.exists(KEY_FILE):
            key = Fernet.generate_key()
            with open(KEY_FILE, "wb") as f:
                f.write(key)
        else:
            with open(KEY_FILE, "rb") as f:
                key = f.read()
        return key

    def save_vault(self, vault: Vault):
        """Encrypt and save vault data to file.

        Args:
            vault (Vault): The vault object containing credentials.
        """
        data = [c.to_dict() for c in vault.list_all()]
        encrypted = self.cipher.encrypt(json.dumps(data).encode())
        with open(VAULT_FILE, "wb") as f:
            f.write(encrypted)

    def load_vault(self) -> Vault:
        """Load and decrypt vault data from file.

        Returns:
            Vault: A vault object populated with stored credentials.
        """
        vault = Vault()
        if os.path.exists(VAULT_FILE):
            with open(VAULT_FILE, "rb") as f:
                encrypted = f.read()
            try:
                decrypted = self.cipher.decrypt(encrypted).decode()
                data = json.loads(decrypted)
                for item in data:
                    vault.add(Credential(item["site"], item["username"], item["password"]))
            except Exception:
                pass  # empty or corrupted vault
        return vault
