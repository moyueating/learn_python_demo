import json
import os

class GameStatus():
  def __init__(self, settings):
    self.settings = settings
    self.reset_status()
    self.game_active = False
    self.read_high_score()

  def reset_status(self):
    self.ships_left = self.settings.ship_limit
    self.score = 0
  
  def read_high_score(self):
    isExists = os.path.exists(self.settings.high_score_file)
    if isExists:
      with open(self.settings.high_score_file) as file:
        self.high_score = json.load(file)
        print(self.high_score)
    else:
      self.high_score = 0