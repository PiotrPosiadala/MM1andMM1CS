class Event():
    
    def __init__(self,event_timestamp=0, event_type=0):
        self.timestamp = event_timestamp
        self.type = event_type

    def __str__(self):
        return('[timestamp=' + str(self.timestamp) + ' type='+ str(self.type) + ']')

    def __repr__(self):
        return str(self)