#Нарисуйте смайлик с помощью написанных функций рисования круга и дуги
if __name__ == '__main__':
    import turtle
    turtle.shape('turtle')
    turtle.speed(0)
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    for i in range(360):
        turtle.forward(1)
        turtle.right(1)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("blue")
    for i in range(360):
        turtle.forward(0.1)
        turtle.right(1)
    turtle.end_fill()
    turtle.penup()
    turtle.backward(60)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("blue")
    for i in range(360):
        turtle.forward(0.1)
        turtle.right(1)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(30)
    turtle.left(90)
    turtle.pendown()
    #turtle.pencolor('red')
    turtle.pensize(5)
    turtle.forward(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.pendown()
    turtle.pencolor('red')
    for i in range(180):
        turtle.forward(0.5)
        turtle.right(1)