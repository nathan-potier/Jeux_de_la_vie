import pygame
import random

# Constantes
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE
FPS = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

class Cell:
    def __init__(self, row, col, alive=False):
        self.row = row
        self.col = col
        self.alive = alive

    def __repr__(self):
        return f"Cell({self.row}, {self.col}, {self.alive})"

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Initialisation de la grille avec des cellules mortes
        self.grid = [[Cell(row, col) for col in range(cols)] for row in range(rows)]

    def get_cell(self, row, col):
        return self.grid[row][col]

    def get_alive_neighbors(self, row, col):

        alive_count = 0
        # Vérifie les 8 cases voisines
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:  # Ignore la cellule elle-même
                    continue
                new_row = row + i
                new_col = col + j
                # Vérifie si les coordonnées sont dans les limites de la grille
                # Compte le nombre de voisins vivants
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.get_cell(new_row, new_col).alive:
                    
                    alive_count += 1
        

        return alive_count

    def update(self):
        # Crée une nouvelle grille pour stocker l'état suivant
        new_grid = [[Cell(row, col) for col in range(self.cols)] for row in range(self.rows)]

        # Applique les règles du jeu de la vie
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[row][col]
                alive_neighbors = self.get_alive_neighbors(row, col)
                if cell.alive:
                    #regle 1, 2, 3 
                    new_grid[row][col].alive = alive_neighbors == 2 or alive_neighbors == 3
                else:
                    #regle 4 de naissance
                    new_grid[row][col].alive = alive_neighbors == 3

        # Met à jour la grille avec le nouvel état
        self.grid = new_grid

    def randomize(self):
        # Initialise la grille avec des cellules vivantes aléatoires
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col].alive = random.choice([True, False])

class GameOfLife:
    def __init__(self, rows, cols):
        self.grid = Grid(rows, cols)
        self.running = False

    def start(self):
        # Démarre le jeu en randomisant la grille
        self.grid.randomize()
        self.running = True

    def update(self):
        # Met à jour la grille si le jeu est en cours
        if self.running:
            self.grid.update()

class Display:
    def __init__(self, width, height, cell_size, game):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.game = game
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Jeu de la Vie")
        self.clock = pygame.time.Clock()

    def draw_grid(self):
        # Dessine chaque cellule de la grille
        for row in range(self.game.grid.rows):
            for col in range(self.game.grid.cols):
                cell = self.game.grid.get_cell(row, col)
                color = GREEN if cell.alive else BLACK
                pygame.draw.rect(
                    self.screen,
                    color,
                    (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                )
        # Dessine les lignes de la grille
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, WHITE, (0, y), (self.width, y))

    def run(self):
        # Démarre le jeu et la boucle principale
        self.game.start()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Met en pause ou reprend le jeu
                        self.game.running = not self.game.running
                    if event.key == pygame.K_r:
                        # Réinitialise la grille
                        self.game.grid.randomize()

            # Met à jour et affiche la grille
            self.game.update()
            self.screen.fill(BLACK)
            self.draw_grid()
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    # Initialisation et lancement du jeu
    game = GameOfLife(ROWS, COLS)
    display = Display(WIDTH, HEIGHT, CELL_SIZE, game)
    display.run()