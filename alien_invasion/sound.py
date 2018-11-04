import pygame

class Sound():
  def __init__(self, settings):
    self.settings = settings
    self.play_bg_music()


  def play_bg_music(self):
    pygame.mixer.init()
    pygame.mixer.music.load(self.settings.bg_music)
    pygame.mixer.music.play()
