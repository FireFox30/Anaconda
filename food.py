import random
import pygame
from settings import *
 
 
class Food:
    def __init__(self, occupied: set, color, shine_color):
        self.pos = self._spawn(occupied)
        self.color = color
        self.shine_color = shine_color
 
    # ── Public ──────────────────────────────────────────────────
    def respawn(self, occupied: set):
        self.pos = self._spawn(occupied)
 
    def draw(self, surface: pygame.Surface):
        x, y = self.pos
        rect = pygame.Rect(x * CELL + 3, y * CELL + 3, CELL - 6, CELL - 6)
        pygame.draw.ellipse(surface, self.color, rect)
        # small shine(255, 100, 100)
        shine = pygame.Rect(x * CELL + 6, y * CELL + 6, 5, 5)
        pygame.draw.ellipse(surface, self.shine_color, shine)
 
    # ── Private ─────────────────────────────────────────────────
    def _spawn(self, occupied: set) -> tuple:
        all_cells = {(c, r) for c in range(COLS) for r in range(ROWS)}
        free = list(all_cells - occupied)
        return random.choice(free)
    

     
     








