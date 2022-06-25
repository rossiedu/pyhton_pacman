# Preparando o ambiente
from turtle import screensize
import pygame
pygame.init()

# Criando a classe para criar a tela do jogo
class Screen():
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

    def cenario_color(self):
        complementary_color = []
        for scale in self.RGB:
            color = 255 - scale
            complementary_color.append(color)
        cenario_color = tuple(complementary_color)
        return cenario_color


# Criando a classe para desenhar o cenario

class Cenario():
    def __init__(self,screen,surface,pacman):
        self.screen = screen
        self. surface = surface
        self.pacman = pacman
        self.matrix = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2],
            [2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2],
            [2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0, 2],
            [2, 0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2],
            [2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2],
            [2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2],
            [2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2],
            [2, 0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0, 2],
            [2, 0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0, 2],
            [2, 0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0, 2],
            [2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2],
            [2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2],
            [2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2],
            [2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0, 2],
            [2, 0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2],
            [2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2],
            [2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]
        self.cell_height = pacman.size
        self.cell_width = pacman.size
        self.path_color = screen.cenario_color()
        self.back_color = screen.background_color()

    def fill_columns(self):
        pass

    def fill_row(self,row_index,row):
        for row_index, row in enumerate(self.matrix):
            for column_index, column in enumerate(row):
                x = column_index * self.cell_height
                y = row_index *  self.cell_width
                if column == 2:
                    pygame.draw.rect(self.surface,self.path_color,(x,y,self.cell_height,self.cell_width),0)
                elif column == 0:
                    pygame.draw.rect(self.surface,self.back_color,(x,y,self.cell_height,self.cell_width),0)

    
    def fill_matrix(self):
        for row_index, row in enumerate(self.matrix):
            self.fill_row(row_index,row)




# Criando a classe pra desenhar o PacMan
class PacMan():
    def __init__(self,screen,surface,color):
        self.size = screen.height // 28
        self.x_center = screen.pacman_center_x()
        self.y_center = screen.pacman_center_y()
        self.background_color = screen.background_color()
        self.screen = screen
        self.surface = surface
        self.color = color
        self.radius = int(self.size / 2)
        self.velocity_x = 0
        self.velocity_y = 0
        self.column = 1
        self.line = 1
# Função para capturar os movimentos 
    def get_events(self,events):
        events = events
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.velocity_x = 1
                elif e.key == pygame.K_LEFT:
                    self.velocity_x = -1
                elif e.key == pygame.K_UP:
                    self.velocity_y = -1
                elif e.key == pygame.K_DOWN:
                    self.velocity_y = 1
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.velocity_x = 0
                elif e.key == pygame.K_LEFT:
                    self.velocity_x = 0
                elif e.key == pygame.K_UP:
                    self.velocity_y = 0
                elif e.key == pygame.K_DOWN:
                    self.velocity_y = 0

    def movement_rules(self):
        self.column += self.velocity_x
        self.line  += self.velocity_y
        self.matrix_size = screen.width // 30
        self.x_center = int(self.column * self.matrix_size + self.radius)
        self.y_center = int(self.line * self.matrix_size)

           
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

# Executando o PacMan
if __name__ =='__main__':
    screen = Screen(1000,1000,(0,0,255))
    surface = screen.create_surface()
    pacman = PacMan(screen,surface,(255,255,0))
    cenario = Cenario(screen,surface,pacman)

    while True:
        pacman.movement_rules()
        surface.fill(screen.cenario_color())
        cenario.fill_matrix()
        pacman.draw_pacman()
        pygame.display.update()
        pygame.time.delay(100)
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
        pacman.get_events(events)
        

        
                    
