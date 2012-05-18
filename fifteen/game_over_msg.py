import pygame.font


class GameOverMessage:
    def draw(self, surface):
        font = pygame.font.Font(None, 50)
        text = font.render('Game Over', True, (255,0,0))
        surface.blit(text, (110, 20))