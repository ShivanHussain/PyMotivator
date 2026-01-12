from twilio_conn import set_twilio_connection, send_whatsapp_message
from quotes import get_quote

client = set_twilio_connection()


def send_daily_quote():
    quote = get_quote()
    send_whatsapp_message(client, quote)
