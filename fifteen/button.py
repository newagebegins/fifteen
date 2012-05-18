import pygame.font

from fifteen.observable import Observable


class Button(Observable):
    def __init__(self, title, x, y):
        Observable.__init__(self)
        self._x = x
        self._y = y
        font = pygame.font.Font(None, 50)
        self._text = font.render(title, True, (255,0,0))
        self._rect = self._text.get_rect(x=self._x, y=self._y)
        self._hover = False
        
    def draw(self, surface):
        if self._hover:
            pygame.draw.rect(surface, (0, 255, 0), self._rect)
        surface.blit(self._text, (self._x, self._y))

    def mouse_motion(self, mouse_pos):
        self._hover = False
        if self._rect.collidepoint(mouse_pos):
            self._hover = True
            
    def mouse_click(self, mouse_pos):
        if self._rect.collidepoint(mouse_pos):
            self.notify()