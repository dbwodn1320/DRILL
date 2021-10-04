from pico2d import *
import math

def handle_events():
    global running,dirX,dirY,mx,my,flag,slope,speedX
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, 600 - 1 - event.y
            speedX = math.sqrt((y - my) * (y - my) + (x - mx)*(x - mx)) // 15
            if y - my != 0 and x - mx != 0:
                slope = (y - my) / (x - mx)

            if mx > x:
                dirX = 1
            elif mx < x:
                dirX = -1
            if my > y:
                dirY = 1
            elif my < y:
                dirY = -1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
open_canvas()
KPU = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cs = load_image('hand_arrow.png')

running = True
hide_cursor()
x = 800 // 2
y = 90
mx = 0
my = 0
frame = 0

speedX = 5
slope = 0

dirX = 0
dirY = 0
heading = 0

while running:
    clear_canvas()
    KPU.draw(400, 300)
    cs.draw(mx, my)
    if dirX == -1:
        character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
        heading = dirX
    elif dirX == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        heading = 0
    elif dirX == 0:
        if dirY == 0:
            character.clip_draw(frame * 100, 300 * 1 + 100*heading, 100, 100, x, y)
        elif heading == 0:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif heading == -1:
            character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)

    if abs(slope) < 1:
        x = x + dirX * speedX
        y = y + (dirX * speedX * slope)
    else:
        x = x + dirY * speedX * (1/slope)
        y = y + (dirY * speedX)

    if dirX == -1 and mx > x:
        dirX = 0
    elif dirX == 1 and mx < x:
        dirX = 0
    if dirY == -1 and my > y:
        dirY = 0
    elif dirY == 1 and my < y:
        dirY = 0

    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    delay(0.02)

close_canvas()

