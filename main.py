from comic_scraper import get_comics_for_date
from az_email_connector import AzEmailConnector
from az_key_vault_connector import AzKeyVaultConnector
from datetime import datetime

emails = ['email@gmail.com']
az_key_vault_connector = AzKeyVaultConnector('DailyComicStripsSecrets')
az_acs_connection_string = az_key_vault_connector.get_secret('AzureAcsConnectionString')
az_acs_sender = az_key_vault_connector.get_secret('AzureAcsSenderEmail')

date = datetime.today()
az_mailer = AzEmailConnector(az_acs_connection_string, az_acs_sender)
comics_html_content = get_comics_for_date(date)

az_mailer.send_email(
    subject= f"Daily comic strip for {date.strftime('%d/%m/%Y')}",
    html_content=comics_html_content,
    to=emails
)