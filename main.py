__author__ = 'william'

import time
import json
import Logger
import messaging as msg


def setup_smores(filename=".twilio_cfg"):

    # Load the Twillio config file

    try:
        creds = json.load(open(filename,'r'))
        msg.account_sid = creds['account_sid']
        msg.auth_token = creds['auth_token']
        msg.phone_number = creds['phone_number']
        msg.twilio_number = creds['twilio_number']

        return creds
    except:
        print "Cant find the crediential file. Look at .twilio_cfg for an example"
        exit()

def create_new_logger(config = None):
    if config == None:
         config = {"hashtag":"test", \
        "type":"rx/tx", \
        "interval":"fixed", \
        "time_regex":"hourly"}

    logger = Logger.Logger(config)
    return logger

if __name__ == "__main__":
    print "Starting to roast some SMoreS"
    creds = setup_smores()

    loggers = []
    loggers.append(create_new_logger())

    #try:
    # See which messages we need to send
    for logger in loggers:
        print "Iterating over loggers"
        if logger.time_to_send(time.localtime()):
            print "Sending data for logger: " + logger.name
            logger.send()
        #send_message(creds)
        msg.check_for_messages()
        # Check for new messages to log
        # Check for messages to send


    time.sleep(60)  # Wait 1 minute

    #except Exception as e:
    #    print e