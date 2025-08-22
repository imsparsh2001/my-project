from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()  # This will load environment variables from a .env file

app = Flask(__name__)

# Get the Key Vault name from environment variables
keyvault_name = os.environ["KEYVAULT_NAME"]  # This environment variable holds the Key Vault name
keyvault_url = f"https://{keyvault_name}.vault.azure.net"

# Use DefaultAzureCredential to authenticate with Azure
credential = DefaultAzureCredential()
client = SecretClient(vault_url=keyvault_url, credential=credential)

# Retrieve the secret from Key Vault
secret_name = "DatabaseConnectionString"  # Replace with the secret name you want to access
try:
    secret = client.get_secret(secret_name)
    secret_value = secret.value
except Exception as e:
    secret_value = f"Error retrieving secret: {e}"

@app.route('/')
def index():
    # Display the secret value fetched from Key Vault or error message
    return f"Hello, Azure! The secret from Key Vault is: {secret_value}"

if __name__ == '__main__':
    app.run(debug=True)
