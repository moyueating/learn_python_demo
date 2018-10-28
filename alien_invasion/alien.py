import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  def __init__(self, settings, screen):
    """初始化单个外星人"""
    super().__init__()
    self.screen = screen
    self.settings = settings

    # 加载外星人图像，并设置其rect属性
    self.image = pygame.image.load('images/alien.bmp')
    self.rect = self.image.get_rect()

    # 每个外星人最初都在屏幕左上角
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    # 存储外星人的准确位置
    self.x = float(self.rect.x)

  def check_edges(self):
    screen_rect = self.screen.get_rect()
    if self.rect.right >= screen_rect.right:
      return True
    elif self.rect.left <= 0:
      return True

  def blitme(self):
    self.screen.blit(self.image, self.rect)
  
  def update(self):
    self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
    self.rect.x = self.x
    