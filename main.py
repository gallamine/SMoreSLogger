__author__ = 'william'

import time
import json
import Logger

def send_message(creds):
    # Download the twilio-python library from http://twilio.com/docs/libraries
    from twilio.rest import TwilioRestClient

    client = TwilioRestClient(creds['account_sid'], creds['auth_token'])

    message = client.messages.create(to=creds['phone_number'], from_=creds['twilio_number'],
                                         body="Hello there!")

def check_for_messages(creds):
    from twilio.rest import TwilioRestClient

    client = TwilioRestClient(creds['account_sid'], creds['auth_token'])

    messages = client.messages.list(
        from_=creds["phone_number"],
    )

    for m in messages:
        print m.sid
        print m.body




def setup_smores(filename=".twilio_cfg"):

    # Load the Twillio config file

    try:
        creds = json.load(open(filename,'r'))
        return creds
    except:
        print "Cant find the crediential file. Look at .twilio_cfg for an example"
        exit()


if __name__ == "__main__":
    print "Starting to roast some SMoreS"
    creds = setup_smores()

    loggers = []
    loggers.append(Logger())

    try:

        #send_message(creds)
        check_for_messages(creds)
        # Check for new messages to log
        # Check for messages to send


        time.sleep(60)  # Wait 1 minute

    except Exception as e:
        print e