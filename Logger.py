__author__ = 'gallamine'

class Logger:

    # A logger can send messages and receive messages. It can do both, or either
    '''
    {"hashtag":"test",
    "type":"rx/tx",
    "interval:"fixed"
    "time_regex":"\d{4}-\d{2}-..."
    '''

    def __init__(self,logger_cfg):
        self.logger_cfg = logger_cfg

    def get_time_to_send(self,current_time):
        #

    def get_message_to_send(self):
        return "The loggers outgoing message"


    def get_response_message(self):
        # Optional
        return "message to send back on succesful reception"
