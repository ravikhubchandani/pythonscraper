from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class AzKeyVaultConnector:
    def __init__(self, key_vault_name: str):
        self.credential = DefaultAzureCredential()
        self.key_vault_url = f"https://{key_vault_name}.vault.azure.net/"
        self.client = SecretClient(vault_url=self.key_vault_url, credential=self.credential)

    def get_secret(self, secret_name: str):
        try:
            retrieved_secret = self.client.get_secret(secret_name)
            return retrieved_secret.value
        
        except Exception as ex:
            print(f"Exception occurred while fetching secret: {ex}")
            return None
