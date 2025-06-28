from azure.communication.email import EmailClient

class AzEmailConnector:
    def __init__(self, connection_string: str, az_acs_sender_email: str):
        self.connection_string = connection_string
        self.az_acs_sender_email = az_acs_sender_email
        self.email_client = EmailClient.from_connection_string(self.connection_string)
                
    def send_email(self, subject: str, html_content: str, to: list[str]):        
        message = {
            "senderAddress": self.az_acs_sender_email,
            "recipients": {
                "to": [{"address": email} for email in to]
            },
            "content": {
                "subject": subject,
                "html": html_content
            }
        }

        try:
            mail = self.email_client.begin_send(message)
            result = mail.result()
            print(f"Email send status: {result['status']}")
        
        except Exception as ex:
            print(f"Exception occurred while sending email: {ex}")
