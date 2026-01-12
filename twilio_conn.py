from twilio.rest import Client # type: ignore
from config import account_sid, auth_token, phone_number


def set_twilio_connection():
    return Client(account_sid, auth_token)


def send_whatsapp_message(client, quote):
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body=quote,
        to=phone_number
    )
    return message.sid
