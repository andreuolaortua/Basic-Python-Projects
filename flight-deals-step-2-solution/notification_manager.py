from twilio.rest import Client

AUTH_TOKEN = ""
APP_SID = ""

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    client = Client(APP_SID, AUTH_TOKEN)
    def send_msg(self, destination_flight):

        client.messages.create(
            from_= ,
            body = f"The flight to {destination_flight}...",
            to =
        )