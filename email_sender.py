import yaml
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class email_sender():

        def send_email(tresc):

                #get secrets
                with open('Projects/fly4free/secrets.yaml', 'r') as secrets_file:
                        secrets_data = yaml.safe_load(secrets_file)
                
                #prepare e-mail body
                message = Mail(
                        from_email=secrets_data['sendgrid']['from_email'],
                        to_emails=secrets_data['sendgrid']['to_emails'],
                        subject='Alert biletowy ze skryptu',
                        html_content=f'<strong>{tresc}</strong>')

                #initialize
                sg = SendGridAPIClient(api_key=secrets_data['sendgrid']['api_key'])

                #send
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)