import pygame


class Button:
    def __init__(self, img, img_hover, x, y, color):
        self.image = img
        self.x = x
        self.y = y
        self.color = color
        self.hover = img_hover

    def draw_button(self, window):
        width, height = self.image.get_rect().size
        pygame.draw.rect(window, self.color, (self.x + 1, self.y + 1, width - 2, height - 2))
        mouse_pos = pygame.mouse.get_pos()
        if self.x < mouse_pos[0] < self.x + width and self.y < mouse_pos[1] < self.y + height:
            window.blit(self.hover, (self.x, self.y))
        else:
            window.blit(self.image, (self.x, self.y))
        pygame.display.update()

    def isClicked(self):
        width, height = self.image.get_rect().size
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x < mouse_pos[0] < self.x + width and self.y < mouse_pos[1] < self.y + height:
            if click[0] == 1:
                return True
        return False


if __name__ == '__main__':
    pygame.init()
    while True:
        print(pygame.key.get_pressed())