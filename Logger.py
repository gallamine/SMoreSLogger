__author__ = 'gallamine'

import time
import messaging as msg


class Logger:

    # A logger can send messages and receive messages. It can do both, or either
    '''
    {"hashtag":"test",
    "type":"rx/tx",
    "interval:"fixed"
    "time_regex":"\d{4}-\d{2}-..."
    "random_type":"uniform"
    '''

    def __init__(self,logger_cfg):
        self.logger_cfg = logger_cfg
        self.last_sent = -1            # -1 means it hasn't been sent yet
        self.name = self.logger_cfg['hashtag']

    def get_message_to_send(self):
        return "The loggers outgoing message"

    def time_to_send(self,current_time):
        if self.logger_cfg['interval'] == "fixed":
            return True
        elif self.logger_cfg['interval'] == "random":
            return randomizer(current_time)
        else:
            print "Invalid interval: " + self.logger_cfg['interval']
            return False


    def get_response_message(self):
        # Optional
        return "message to send back on succesful reception"

    def send(self):
        # send the message
        message = self.get_message_to_send()
        msg.send_message(message)
        self.last_sent = time.localtime()
        return True

    def _randomizer(self,current_time,random_type):
        if self.logger_cfg['random_type'] == "normal":
            return True
        elif self.logger_cfg['random_type'] == "poisson":
            return True
        elif self.logger_cfg['random_type'] == "gaussian":
            return True
        else:
            return False

