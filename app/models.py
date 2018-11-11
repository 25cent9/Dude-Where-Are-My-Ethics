class Player(object):

    MORALLY_GOOD = "MG"
    NEUTRAL = "N"
    MORALLY_BAD = "MB"

    def __init__(self, username, moral_state = "MG"):
        self.username = username
        self.moral_state = moral_state
    
    def ChangeState(self, moral_value):
        if(moral_value >= 75):
            self.moral_state = self.MORALLY_GOOD
        elif(moral_value == 50):
            self.moral_state = self.NEUTRAL
        else:
            self.moral_state = self.MORALLY_BAD