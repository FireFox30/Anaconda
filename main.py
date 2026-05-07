import pygame, random
from settings import *
from snake import Snake
from food import Food



 
HUD_H = 25  # height of score bar in pixels
 
 
def draw_grid(surface):
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(surface, GRID_LINE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(surface, GRID_LINE, (0, y), (WIDTH, y))
 
 
def draw_hud(surface, font, score, best):
    s = font.render(f"SCORE  {score:04d}", True, SCORE_COLOR)
    b = font.render(f"BEST   {best:04d}",  True, SCORE_COLOR)
    surface.blit(s, (10, 10))
    surface.blit(b, (WIDTH - b.get_width() - 10, 10))
 
 
def draw_overlay(surface, big_font, small_font, text, sub):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    surface.blit(overlay, (0, 0))
    t = big_font.render(text, True, GAME_OVER_C)
    s = small_font.render(sub,  True, SCORE_COLOR)
    surface.blit(t, t.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 28)))
    surface.blit(s, s.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
 
 
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT + HUD_H))
    pygame.display.set_caption("Snake")
    clock  = pygame.time.Clock()   # use pygame.time.Clock() for compatibility
 
    big_font   = pygame.font.SysFont("consolas", 42, bold=True)
    small_font = pygame.font.SysFont("consolas", 20)
    hud_font   = pygame.font.SysFont("consolas", 16)
 
    # Separate surfaces so drawing offsets stay simple
    game_surf = pygame.Surface((WIDTH, HEIGHT))
    hud_surf  = pygame.Surface((WIDTH, HUD_H))
 
    DIR_MAP = {
        pygame.K_UP:    UP,    pygame.K_w: UP,
        pygame.K_DOWN:  DOWN,  pygame.K_s: DOWN,
        pygame.K_LEFT:  LEFT,  pygame.K_a: LEFT,
        pygame.K_RIGHT: RIGHT, pygame.K_d: RIGHT,
    }
 
    snake = Snake()
    food  = Food(snake.cells(),(199,55,47), (240,105,97))
    food2 = Food(snake.cells(), (0, 65, 194), (24, 105, 234))
    score = 0
    best  = 0
    state = "playing"
 
    while True:
        # ── Events ────────────────────────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    raise SystemExit
                if state == "playing" and event.key in DIR_MAP:
                    snake.set_direction(DIR_MAP[event.key])
                if state == "dead" and event.key == pygame.K_RETURN:
                    snake.reset()
                    food  = Food(snake.cells())
                    score = 0
                    state = "playing"
 
        # ── Update ────────────────────────────────────────────
        if state == "playing":
            new_head = snake.move()
            if not snake.alive:
                best  = max(best, score)
                state = "dead"
            elif new_head == food.pos:
                snake.grow()
                score += 1
                food.respawn(snake.cells())
                
            elif new_head == food2.pos:
                snake.grow()
                score += 2
                food2.respawn(snake.cells())
                
        choices = food.pos, food.pos, food.pos, food.pos, food2.pos
        cointtoss=random.choices(choices)
        
 
        # ── Draw game surface ──────────────────────────────────
        game_surf.fill(BG)
        draw_grid(game_surf)
        food.draw(game_surf)
        food2.draw(game_surf)
        snake.draw(game_surf)
        if state == "dead":
            draw_overlay(game_surf, big_font, small_font,
                         "GAME OVER", f"Score: {score}   ENTER to restart")
 
        # ── Draw HUD surface ───────────────────────────────────
        hud_surf.fill((10, 12, 16))
        draw_hud(hud_surf, hud_font, score, best)
 
        # ── Compose onto screen ────────────────────────────────
        screen.blit(hud_surf,  (0, 0))
        screen.blit(game_surf, (0, HUD_H))
        pygame.display.flip()
        clock.tick(FPS)
 
 
if __name__ == "__main__":
    main()