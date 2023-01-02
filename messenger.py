from twilio.rest import Client

class Messenger:
    def __init__(self, account_sid, auth_token, from_number, to_number) -> None:
        self.client = Client(account_sid, auth_token)
        self.FROM_NUMBER = from_number
        self.TO_NUMBER = to_number
        
    def message(self, message):
        message = self.client.messages.create(
            body=message,
            from_=self.FROM_NUMBER,
            to=self.TO_NUMBER
        )
        
        print(message.sid)