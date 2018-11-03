import pygame.font

class ScoreBoard():

  def __init__(self, settings, screen, status):
    self.screen = screen
    self.screen_rect = screen.get_rect()
    self.settings = settings
    self.status = status

    self.text_color = (0, 0, 0)
    self.font = pygame.font.SysFont(None, 48)

    self.prep_score()

  def prep_score(self):
    round_score = round(self.status.score, -1)
    score_str = "当前得分：" + "{:,}".format(round_score)
    self.score_img = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

    # 得分在右上角
    self.score_rect = self.score_img.get_rect()
    self.score_rect.right = self.screen_rect.right - 20
    self.score_rect.top = 20

  def show_score(self):
    self.screen.blit(self.score_img, self.score_rect)