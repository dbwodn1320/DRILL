from pico2d import *
import math

def Renering(x,y):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
deg = 270
cnt = 0
move_direction = 0
RectOrCircle = 0
while 1:
    Renering(x,y)

    if RectOrCircle == 0:
        if move_direction == 0 :
            if cnt == 1:
                if x > 400:
                    RectOrCircle = 1
                    cnt = 0
            if x < 780:
                x += 2
            else:
                move_direction += 1

        elif move_direction == 1 :
            if y < 560:
                y += 2
            else:
                move_direction += 1

        elif move_direction == 2 :
            if x > 20:
                x -= 2
            else:
                move_direction += 1
                
        elif move_direction == 3 :
            if y > 90:
                y -= 2
            else:
                move_direction = 0
                cnt += 1

    if RectOrCircle == 1:
        x = math.cos(deg/180*math.pi)*210 + 400
        y = math.sin(deg/180*math.pi)*210 + 300
        deg += 1
        if deg == 270 + 360:
            deg = 270
            RectOrCircle = 0

    delay(0.01)   

close_canvas()
