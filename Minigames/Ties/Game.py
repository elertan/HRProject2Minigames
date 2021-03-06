from Minigame import Minigame

class TiesGame(Minigame):
    def __init__(self):
        super(TiesGame, self).__init__("TiesGame", "Ties", 5)
    
    # When a player starts this minigame
    def enter(self):
        raise NotImplementedError("You need to override the enter method on your minigame.")

    # When a player leaves this minigame
    def leave(self):
        raise NotImplementedError("You need to override the leave method on your minigame.")

    def handleEvents(self, events):
        raise NotImplementedError("You need to override the handleEvents method on your minigame.")

    # Gets called on every frame
    def update(self, dt):
        raise NotImplementedError("You need to override the update method on your minigame.")

    # Gets called on every frame
    def updatePreview(self, dt):
        raise NotImplementedError("You need to override the updatePreview method on your minigame.")

    # Draw the current game state
    def draw(self, surface):
        raise NotImplementedError("You need to override the draw method on your minigame.")

    def drawPreview(self, surface):
        raise NotImplementedError("You need to override the drawPreview method on your minigame.")