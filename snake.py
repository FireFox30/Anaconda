from collections import deque
import pygame
from settings import *
 
 
class Snake:
    def __init__(self):
        self.reset()
 
    # ── Public ──────────────────────────────────────────────────
    def reset(self):
        cx, cy = COLS // 2, ROWS // 2
        self.body      = deque([(cx, cy), (cx - 1, cy), (cx - 2, cy)])
        self.direction = RIGHT
        self._next_dir = RIGHT
        self.alive     = True
        self.grew      = False
 
    def set_direction(self, new_dir: tuple):
        """Buffer the next direction; ignore reversal."""
        opposites = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}
        if new_dir != opposites[self.direction]:
            self._next_dir = new_dir
 
    def move(self) -> tuple:
        """Advance one step. Returns new head position."""
        self.direction = self._next_dir
        hx, hy = self.body[0]
        dx, dy = self.direction
        new_head = (hx + dx, hy + dy)
 
        # Wall collision
        if not (0 <= new_head[0] < COLS and 0 <= new_head[1] < ROWS):
            self.alive = False
            return new_head
 
        # Self collision
        if new_head in self.cells():
            self.alive = False
            return new_head
 
        self.body.appendleft(new_head)
        if not self.grew:
            self.body.pop()
        self.grew = False
        return new_head
 
    def grow(self):
        self.grew = True
       
 
    def cells(self) -> set:
        return set(self.body)
 
    def draw(self, surface: pygame.Surface):
        for i, (x, y) in enumerate(self.body):
            color  = SNAKE_HEAD if i == 0 else SNAKE_BODY
            margin = 2 if i == 0 else 3
            rect   = pygame.Rect(
                x * CELL + margin,
                y * CELL + margin,
                CELL - margin * 2,
                CELL - margin * 2,
            )
            radius = 6 if i == 0 else 4
            pygame.draw.rect(surface, color, rect, border_radius=radius)
 
            # Eyes on the head
            if i == 0:
                self._draw_eyes(surface, x, y)
 
    # ── Private ─────────────────────────────────────────────────
    def _draw_eyes(self, surface, gx, gy):
        dx, dy = self.direction
        cx = gx * CELL + CELL // 2
        cy = gy * CELL + CELL // 2
 
        # Perpendicular offset for eye spread
        px, py = -dy, dx  # rotate direction 90°
 
        for sign in (+1, -1):
            ex = cx + dx * 5 + sign * px * 5
            ey = cy + dy * 5 + sign * py * 5
            pygame.draw.circle(surface, (20, 20, 20), (ex, ey), 3)
            pygame.draw.circle(surface, (255, 255, 255), (ex - 1, ey - 1), 1)
 