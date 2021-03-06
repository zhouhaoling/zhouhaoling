import sys
import pygame
from alien import Alien
from settings import Settiongs
from ship import Ship
from bullet import Bullet

SCREEN_SIZE = (1200,800)

class AlienInvasion:
    """管理有限资源合行为"""

    def __init__(self):
        """初始化pyagem"""
        pygame.init()
        self.settings = Settiongs()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height),pygame.RESIZABLE
        )
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self):
        """创建外星人"""
        alien = Alien(self)
        self.aliens.add(alien)

    def run_game(self):
        #设置背景图片
        background = pygame.image.load(r'pythonTest\universe.jpg').convert()
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen(background)


    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    SCREEN_SIZE = event.size
                    self.screen = pygame.display.set_mode(SCREEN_SIZE,pygame.RESIZABLE)
                    pygame.display.update()
                #左右移动 
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
                
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """创建一颗子弹，并加入编组bullets中"""
        # 限制子弹数量
        # if len(self.bullets)<self.settings.bullet_allowed:
        #     new_bullet = Bullet(self)
        #     self.bullets.add(new_bullet)
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """更新子弹位置"""
        self.bullets.update()
        """删除消失的子弹"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _update_screen(self,background):
            # self.screen.fill(self.settings.bg_color)
            # 在屏幕上绘制飞船
            self.screen.blit(background,(0,0))
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)
            pygame.display.update()     


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
