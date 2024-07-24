class Logger:

    def __init__(self):
        self.history = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message is not None and message not in self.history.keys():
            self.history[message] = timestamp
            return True
        else:
            prev_timestamp = self.history[message]
            if timestamp - prev_timestamp == 0:
                return False
            elif timestamp - prev_timestamp >= 10:
                self.history[message] = timestamp
                return True
            else:
                return False


