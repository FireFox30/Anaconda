# ── Window & Grid ──────────────────────────────────────────────
CELL        = 24          # pixels per grid cell
COLS        = 30         # grid columns
ROWS        = 24          # grid rows
WIDTH       = CELL * COLS
HEIGHT      = CELL * ROWS
FPS         = 9         # snake moves per second
 
# ── Colours ────────────────────────────────────────────────────
BLACK       = (  0,   0,   0)
BG          = ( 15,  17,  21)   # near-black background
GRID_LINE   = ( 25,  28,  35)   # subtle grid lines
SNAKE_HEAD  = ( 80, 220, 120)   # bright green head
SNAKE_BODY  = ( 50, 170,  90)   # slightly darker body
FOOD_COLOR  = (230,  70,  70)   # red food
SCORE_COLOR = (200, 210, 225)   # light text
GAME_OVER_C = (230,  70,  70)
 
# ── Directions (dx, dy) ────────────────────────────────────────
UP    = ( 0, -1)
DOWN  = ( 0,  1)
LEFT  = (-1,  0)
RIGHT = ( 1,  0)
 
