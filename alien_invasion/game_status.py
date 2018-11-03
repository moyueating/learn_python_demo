

class GameStatus():
  def __init__(self, settings):
    self.settings = settings
    self.reset_status()
    self.game_active = False

  def reset_status(self):
    self.ships_left = self.settings.ship_limit
    self.score = 0