import pygame.font


class GameOverMessage:
    def draw(self, surface):
        font = pygame.font.Font('freesansbold.ttf', 45)
        text = font.render('Game Over', True, (255,0,0))
        surface.blit(text, (75, 20))