import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard():

  def __init__(self, settings, screen, status):
    self.screen = screen
    self.screen_rect = screen.get_rect()
    self.settings = settings
    self.status = status
    self.bg_color = "transparent"
    self.text_color = (0, 0, 0)
    self.font = pygame.font.SysFont("stfangsong", 20)

    self.prep_score()
    self.prep_high_score()
    self.prep_life()

  def prep_score(self):
    round_score = round(self.status.score, -1)
    score_str = "当前得分：" + "{:,}".format(round_score)
    self.score_img = self.font.render(score_str, True, self.text_color, self.bg_color)

    # 得分在右上角
    self.score_rect = self.score_img.get_rect()
    self.score_rect.right = self.screen_rect.right - 20
    self.score_rect.top = 10
  
  def prep_high_score(self):
    hign_score = round(self.status.high_score, -1)
    hign_score_str = "历史最高分：" + "{:,}".format(hign_score)
    self.high_score_image = self.font.render(hign_score_str, True, self.text_color, self.bg_color)

    self.high_score_rect = self.high_score_image.get_rect()
    self.high_score_rect.center = self.screen_rect.center
    self.high_score_rect.top = self.score_rect.top

  def prep_life(self):
    # life_str = "剩余生命：" + str(self.status.ships_left)
    # self.life_img = self.font.render(life_str, True, self.text_color, self.bg_color)
    # self.life_rect = self.life_img.get_rect()
    # self.life_rect.left = self.screen_rect.left + 20
    # self.life_rect.top = self.score_rect.top
    self.ships = Group()
    for ship_number in range(self.status.ships_left):
      ship = Ship(self.settings, self.screen)
      ship.rect.x = 10 + ship_number * (ship.rect.width + 5)
      ship.rect.y = 5
      self.ships.add(ship)

  def show_score(self):
    self.screen.blit(self.score_img, self.score_rect)
    self.screen.blit(self.high_score_image, self.high_score_rect)
    # self.screen.blit(self.life_img, self.life_rect)
    self.ships.draw(self.screen)