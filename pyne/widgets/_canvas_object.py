import pygame as pg


class CanvasObject:
    def __init__(self, info):
        self.info = info

        match info[0]:
            case 'point':
                self.rect = pg.Rect(info[1][0], info[1][1], 1, 1)

                self.x = info[1][0]
                self.y = info[1][1]

                self.color = info[2]
            case 'line':
                self.end_pos = info[2]

                self.x = info[1][0]
                self.y = info[1][1]

                self.color = info[3]

                self.line_width = info[4]
            case 'rect':
                self.rect = pg.Rect(info[1][0], info[1][1], info[2], info[3])

                self.x = info[1][0]
                self.y = info[1][1]

                self.color = info[4]
            case 'circle':
                self.x = info[1][0]
                self.y = info[1][1]

                self.R = info[2]

                self.color = info[3]

    def draw(self, screen: pg.Surface):
        match self.info[0]:
            case 'point':
                self.rect.x = self.x
                self.rect.y = self.y

                pg.draw.rect(screen, self.color, self.rect)
            case 'line':
                pg.draw.line(screen, self.color, (self.x, self.y), self.end_pos, self.line_width)
            case 'rect':
                self.rect.x = self.x
                self.rect.y = self.y

                pg.draw.rect(screen, self.color, self.rect)
            case 'circle':
                pg.draw.circle(screen, self.color, (self.x, self.y), self.R)
