__author__ = 'william'

account_sid = []
auth_token = []
phone_number = []
twilio_number = []

def send_message(message):
    # Download the twilio-python library from http://twilio.com/docs/libraries
    from twilio.rest import TwilioRestClient

    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to=phone_number, from_=twilio_number,
                                         body=message)

def check_for_messages():
    from twilio.rest import TwilioRestClient

    client = TwilioRestClient(account_sid, auth_token)

    messages = client.messages.list(
        from_=creds["phone_number"],
    )

    for m in messages:
        print m.sid
        print m.body
