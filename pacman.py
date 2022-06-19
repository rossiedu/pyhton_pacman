# Preparando o ambiente
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


class pacman():
    def __init__(self,tamanho,screen,surface,color):
        self.tamanho = tamanho
        self.x_center = screen.pacman_center_x()
        self.y_center = screen.pacman_center_y()
        self.background_color = screen.background_color()
        self.screen = screen
        self.surface = surface
        self.color = color
        self.radius = tamanho / 2

    def draw_circle(self):
        surface = self.surface
        color = self.color
        radius = self.radius
        x_center = self.x_center
        y_center = self.y_center
        circle = pygame.draw.circle(surface,color,(x_center,y_center),radius,0)
        return circle
    
    def draw_polygon(self):
       color_black = (0,0,0)
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
        radius = int(self.radius / 10)
        x_center = int(self.x_center + (self.radius / 2))
        y_center = int(self.y_center - (self.radius / 2))
        small_circle = pygame.draw.circle(surface,color,(x_center,y_center),radius,0)
        return small_circle

    