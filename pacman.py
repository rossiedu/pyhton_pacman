# Preparando o ambiente
from turtle import screensize
import pygame
pygame.init()

class create_screen():
    def __init__(self,width,height,rgb_color):
        self.width = width
        self.height = height
        self.RGB = rgb_color
    
    def create_surface(self):
        screen = pygame.display.set_mode(
            (self.width,self.height),
            0
        )
        screen.fill(self.RGB)
        pygame.display.flip()
        return screen

    def pacman_center_x(self):
        x_center = self.width / 2
        return x_center

    def pacman_center_y(self):
        y_center = self.height / 2
        return y_center

    def background_color(self):
        color = self.RGB
        return color
    


class PacMan():
    def __init__(self,size,screen,surface,color):
        self.size = size
        self.x_center = screen.pacman_center_x()
        self.y_center = screen.pacman_center_y()
        self.background_color = screen.background_color()
        self.screen = screen
        self.surface = surface
        self.color = color
        self.radius = int(size / 2)
        self.velocity_x = 0.4
        self.velocity_y = 0.4
        self.column = 1
        self.line = 1

    def movement_rules(self):
        self.column += self.velocity_x
        self.line  += self.velocity_y
        self.matrix_size = screen.width // 30
        self.x_center = int(self.column * self.matrix_size + self.radius)
        self.y_center = int(self.line * self.matrix_size)

        if self.x_center + self.radius > screen.width:
            self.velocity_x -= 0.4

        if self.x_center - self.radius < 0:
            self.velocity_x += 0.4
        if self.y_center + self.radius > screen.height:
            self.velocity_y -= 0.4

        if self.y_center - self.radius < 0:
            self.velocity_y += 0.4
           
    def draw_circle(self):
        surface = self.surface
        color = self.color
        radius = self.radius
        x_center = self.x_center
        y_center = self.y_center
        circle = pygame.draw.circle(surface,color,(x_center,y_center),radius,0)
        return circle
    
    def draw_polygon(self):
       point_one = (self.x_center,self.y_center)
       point_two = (self.x_center + self.radius, self.y_center - self.radius)
       point_three = (self.x_center + self.radius, self.y_center)
       surface = self.surface
       dots = [point_one,point_two,point_three]
       polygon = pygame.draw.polygon(surface,self.background_color,dots,0)
       return polygon
    
    def draw_small_circle(self):
        surface = self.surface
        color = (0,0,0)
        radius = int(self.radius / 8)
        x_center = int(self.x_center + (self.radius / 3))
        y_center = int(self.y_center - (self.radius * 0.70))
        small_circle = pygame.draw.circle(surface,color,(x_center,y_center),radius,0)
        return small_circle
    @classmethod
    def draw_pacman(self):
        body = pacman.draw_circle()
        mounth = pacman.draw_polygon()
        eye = pacman.draw_small_circle()
        return body,mounth,eye

if __name__ =='__main__':
    screen = create_screen(800,600,(0,0,0))
    surface = screen.create_surface()
    pacman = PacMan(50,screen,surface,(255,255,0))
    while True:
        pacman.movement_rules()
        surface.fill((0,0,0))
        pacman.draw_pacman()
        pygame.display.update()
        pygame.time.delay(100)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()