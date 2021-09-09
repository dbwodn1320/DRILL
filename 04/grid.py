import turtle

turtle.penup()
turtle.goto(-250,250)

count = 6
while(count > 0):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(-250,250-100*(7 - count))
    count -= 1

turtle.penup()
turtle.goto(-250,250)

count = 6
turtle.right(90)
while(count > 0):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(-250+100*(7 - count),250)
    count -= 1

turtle.exitonclick()
