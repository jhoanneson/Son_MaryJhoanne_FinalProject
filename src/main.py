#src/main.py
"""
Module: main.py
Purpose: CLI interface for the Password Manager.
"""

from models import Credential, Vault
from storage import StorageManager


def menu():
    """Display the main menu options."""
    print("\n--- Password Manager CLI ---")
    print("1. Add Credential")
    print("2. List Credentials")
    print("3. Find Credential")
    print("4. Exit")


def main():
    """Run the CLI Password Manager.

    Provides options to add, list, and find credentials.
    """
    storage = StorageManager()
    vault = storage.load_vault()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            site = input("Site: ")
            username = input("Username: ")
            password = input("Password: ")
            vault.add(Credential(site, username, password))
            storage.save_vault(vault)
            print("✅ Credential added successfully!")

        elif choice == "2":
            creds = vault.list_all()
            if creds:
                for c in creds:
                    print(f"Site: {c.site} | Username: {c.username}")
            else:
                print("No credentials stored.")

        elif choice == "3":
            site = input("Enter site to search: ")
            results = vault.find(site)
            if results:
                for c in results:
                    print(f"Site: {c.site} | Username: {c.username} | Password: {c.password}")
            else:
                print("No credentials found for that site.")

        elif choice == "4":
            print("Exiting Password Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
