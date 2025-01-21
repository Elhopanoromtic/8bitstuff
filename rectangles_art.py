import turtle
import math

def draw_square(turtle, length):
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)

def draw_rectangle(turtle, width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def main():
    window = turtle.Screen()
    sizex=1200
    sizey=900
    window.setup(sizex, sizey)

    my_turtle = turtle.Turtle()
    window.bgcolor("white")

    #  speed up drawing
    my_turtle.speed(0)
    my_turtle.hideturtle()
    turtle.tracer(0, 0) 
    my_turtle.color('black')
    # TODO add error checking for extreme values of sizex
    spready=sizey/2-sizex/15
    sizexh=sizex/2

    for i in range(int(sizex*0.9)):            
            # Move to the starting position
            my_turtle.penup()
            my_turtle.goto(i-sizexh, spready*math.cos(i)+i/30)
            my_turtle.pendown()

            # Draw the rectangle
            draw_rectangle(my_turtle, i/10, i/15)
            #print(f'%.2f' % (spready*math.cos(i)+ycorrection))

    turtle.update
    window.mainloop()

if __name__ == "__main__":
    main()